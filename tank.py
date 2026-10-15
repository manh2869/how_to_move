import pygame
import pymunk
import move
import physics
import math
import collect_data


def draw_box(screen, body, shape, color):
    points = [body.local_to_world(v) for v in shape.get_vertices()]
    points = [(int(p.x), int(p.y)) for p in points]
    pygame.draw.polygon(screen, color, points)


def aim_at(tank_body, target_body):
    dx = target_body.position.x - tank_body.position.x
    dy = target_body.position.y - tank_body.position.y

    angle = math.atan2(dy, dx)

    tank_body.angle = angle


BULLET = 1
TARGET = 2


def shoot(space, tank_body, rec_radius, barrel_len):
    tip = tank_body.local_to_world((rec_radius + barrel_len + 6, 0))

    bullet_body, bullet_shape = physics.create_ball(
        space, position=tip, mass=1, radius=5
    )
    bullet_shape.collision_type = BULLET
    bullet_body.velocity = pymunk.Vec2d(1200, 0).rotated(tank_body.angle)

    return bullet_body, bullet_shape


# def move_to_distance(tank_body, target_body, target_distance, speed):
#     dx = target_body.position.x - tank_body.position.x
#     dy = target_body.position.y - tank_body.position.y
#     distance = math.sqrt(dx**2 + dy**2)
#     if distance <= target_distance:
#         tank_body.velocity = (0, 0)
#         return
#     direction = pymunk.Vec2d(dx, dy).normalized()
#     tank_body.velocity = direction * speed


def check_hit(enemy_shape, bullet_shape):
    point = enemy_shape.point_query(bullet_shape.body.position)
    return point.distance <= 5


def get_target_speed(target_body, previous_pos, dt):
    x, y = target_body.position
    old_x, old_y = previous_pos

    vx = (x - old_x) / dt
    vy = (y - old_y) / dt

    speed = math.sqrt(vx**2 + vy**2)

    return vx, vy, speed


pygame.init()

W = 1200
H = 900

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("tank")

clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 0)
space.damping = 0.6

rec_radius = 25
r_main_body, r_main_shape = physics.create_box(
    space, position=(100, 600), mass=10, width=rec_radius * 2, height=rec_radius * 2
)

r_body, r_shape = physics.create_box(
    space, position=(900, 400), mass=1, width=rec_radius * 2, height=rec_radius * 2
)
pre_pos = r_body.position

r_shape.collision_type = TARGET


def on_bullet_hit(arbiter, space, data):
    a, b = arbiter.shapes
    for s, other in ((a, b), (b, a)):
        if s.collision_type == BULLET:
            finished.setdefault(s, 1 if other.collision_type == TARGET else 0)


space.on_collision(BULLET, None, begin=on_bullet_hit)
barrel_len = 40
barrel_w = 10

barrel_shape = pymunk.Poly(
    r_main_body,
    [
        (rec_radius, -barrel_w / 2),
        (rec_radius + barrel_len, -barrel_w / 2),
        (rec_radius + barrel_len, barrel_w / 2),
        (rec_radius, barrel_w / 2),
    ],
)
space.add(barrel_shape)


ground_shape = physics.create_wall(space, 0, H, W, H, 10)
ground_shape = physics.create_wall(space, 0, 0, 0, H, 10)
ground_shape = physics.create_wall(space, W, 0, W, H, 10)
ground_shape = physics.create_wall(space, 0, 0, W, 0, 10)


running = True
speed = 300
attack = False

bullet = []
finished = {}

collect_data.create_csv()
shoot_timer = 0
shoot_interval = 0.5
hit = 0
data_timer = 0
data_interval = 0.5


while running:

    dt = clock.tick(120) / 1000.0

    # mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         tip = r_main_body.local_to_world((rec_radius + barrel_len + 6, 0))
        #         bullet_body, bullet_shape = physics.create_ball(
        #             space, position=tip, mass=1, radius=5
        #         )
        #         bullet_body.velocity = pymunk.Vec2d(1200, 0).rotated(r_main_body.angle)
        #         bullet.append((bullet_body, bullet_shape))

    # move.move1(r_main_body, 300)

    # move_to_distance(r_main_body, r_body, 600, 200)
    aim_at(r_main_body, r_body)

    shoot_timer += dt

    space.step(1 / 120)
    screen.fill((30, 30, 30))

    for b in bullet:
        pygame.draw.circle(screen, (255, 0, 0), (b[0].position), 5)

    r_x, r_y = r_body.position
    r_main_x, r_main_y = r_main_body.position
    vx, vy, speedt = get_target_speed(r_body, pre_pos, dt)
    pre_pos = r_body.position
    if shoot_timer > shoot_interval:
        b = shoot(space, r_main_body, rec_radius, barrel_len)
        bullet.append(
            (b[0], b[1], collect_data.make_state(r_main_body, r_body, vx, vy, speedt))
        )
        shoot_timer = 0

    for b in bullet[:]:
        body, shape, state = b
        x, y = body.position

        if shape in finished:
            collect_data.save_data(state, finished[shape])
            space.remove(body, shape)
            bullet.remove(b)
    finished.clear()

    draw_box(screen, r_body, r_shape, (100, 100, 100))
    draw_box(screen, r_main_body, r_main_shape, (100, 200, 100))
    draw_box(screen, r_main_body, barrel_shape, (200, 200, 200))
    pygame.draw.line(screen, (200, 200, 200), (0, H), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (0, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (W, 0), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (W, 0), 20)

    pygame.display.flip()

pygame.quit()
