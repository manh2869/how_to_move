import pymunk
import time
import pygame


def create_ball(space, position, mass=1, radius=25):
    moment = pymunk.moment_for_circle(mass, 0, radius)

    body = pymunk.Body(mass, moment)
    body.position = position

    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.75
    shape.friction = 1

    space.add(body, shape)

    return [body, shape]


def create_box(space, position, mass=1, width=80, height=80):
    moment = pymunk.moment_for_box(mass, (width, height))

    body = pymunk.Body(mass, moment)
    body.position = position

    shape = pymunk.Poly.create_box(body, (width, height))
    shape.elasticity = 0.75
    shape.friction = 1

    space.add(body, shape)

    return body, shape


def create_wall(space, x, y, x1, y1, radius=10):
    shape = pymunk.Segment(space.static_body, (x, y), (x1, y1), radius)

    shape.friction = 1
    shape.elasticity = 0.75

    space.add(shape)

    return shape


def create_barrel(space, r_main_body, rec_radius, barrel_len=40, barrel_w=10):
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
    return barrel_shape


def create_ground(space, W, H):
    create_wall(space, 0, H, W, H, 10)
    create_wall(space, 0, 0, 0, H, 10)
    create_wall(space, W, 0, W, H, 10)
    create_wall(space, 0, 0, W, 0, 10)


def shoot(space, screen, r_main_body, bullet, rec_radius, running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tip = r_main_body.local_to_world((rec_radius + 40 + 6, 0))
                bullet_body, bullet_shape = create_ball(
                    space, position=tip, mass=1, radius=5
                )
                bullet_body.velocity = pymunk.Vec2d(1200, 0).rotated(r_main_body.angle)
                bullet.append((bullet_body, bullet_shape, time.time()))
    for b in bullet:
        pygame.draw.circle(screen, (0, 255, 0), (b[0].position), 5)
        if time.time() - b[2] >= 7:
            space.remove(b[0], b[1])
            bullet.remove(b)
    return running
