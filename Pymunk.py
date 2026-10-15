import pymunk


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
    # barrel_len = 40
    # barrel_w = 10
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
