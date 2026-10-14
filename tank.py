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


def shoot(space, tank_body, rec_radius, barrel_len):
    tip = tank_body.local_to_world((rec_radius + barrel_len + 6, 0))

    bullet_body, bullet_shape = physics.create_ball(
        space, position=tip, mass=1, radius=5
    )

    bullet_body.velocity = pymunk.Vec2d(1200, 0).rotated(tank_body.angle)

    return bullet_body, bullet_shape


def move_to_distance(tank_body, target_body, target_distance, speed):
    dx = target_body.position.x - tank_body.position.x
    dy = target_body.position.y - tank_body.position.y
    distance = math.sqrt(dx**2 + dy**2)
    if distance <= target_distance:
        tank_body.velocity = (0, 0)
        return
    direction = pymunk.Vec2d(dx, dy).normalized()
    tank_body.velocity = direction * speed


def check_hit(enemy_shape, bullet_shape):
    point = enemy_shape.point_query(bullet_shape.body.position)
    return point.distance <= 5


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
r1_body, r1_shape = physics.create_box(
    space, position=(100, 600), mass=10, width=rec_radius * 2, height=rec_radius * 2
)

r_body, r_shape = physics.create_box(
    space, position=(900, 400), mass=1, width=rec_radius * 2, height=rec_radius * 2
)

barrel_len = 40
barrel_w = 10

barrel_shape = pymunk.Poly(
    r1_body,
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
collect_data.create_csv()
shoot_timer = 0
shoot_interval = 0.5
hit = 0
data_timer = 0
data_interval = 0.5
while running:
    dt = clock.tick(120) / 1000.0
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tip = r1_body.local_to_world((rec_radius + barrel_len + 6, 0))
                bullet_body, bullet_shape = physics.create_ball(
                    space, position=tip, mass=1, radius=5
                )
                bullet_body.velocity = pymunk.Vec2d(1200, 0).rotated(r1_body.angle)
                bullet.append((bullet_body, bullet_shape))

    # move.move1(r1_body, 300)

    move_to_distance(r1_body, r_body, 600, 200)
    aim_at(r1_body, r_body)

    shoot_timer += dt

    space.step(1 / 120)
    screen.fill((30, 30, 30))

    for b in bullet:
        pygame.draw.circle(screen, (255, 0, 0), (b[0].position), 5)

    # print(r1_body.position, r1_body.angle, r_body.position, r_body.angle)

    data_timer += dt

    if shoot_timer > shoot_interval:
        b = shoot(space, r1_body, rec_radius, barrel_len)
        bullet.append(b)
        shoot_timer = 0
    for b in bullet[:]:
        if check_hit(r_shape, b[1]):
            if data_timer >= data_interval:
                collect_data.save_data(r1_body, r_body, 1)
                data_timer = 0
        else:
            if data_timer >= data_interval:
                collect_data.save_data(r1_body, r_body, 1)
                data_timer = 0
        body, shape = b
        x, y = body.position
        if x > W - 20 or x < 20 or y > H - 20 or y < 20:
            space.remove(body, shape)
            bullet.remove(b)

    r_x, r_y = r_body.position
    r1_x, r1_y = r1_body.position

    draw_box(screen, r_body, r_shape, (100, 100, 100))
    draw_box(screen, r1_body, r1_shape, (100, 200, 100))
    draw_box(screen, r1_body, barrel_shape, (200, 200, 200))
    pygame.draw.line(screen, (200, 200, 200), (0, H), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (0, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (W, 0), (W, H), 20)
    pygame.draw.line(screen, (200, 200, 200), (0, 0), (W, 0), 20)

    pygame.display.flip()

pygame.quit()
