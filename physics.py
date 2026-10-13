
import pymunk


def create_ball(space, position, mass=1, radius=25):
    moment = pymunk.moment_for_circle(
        mass, 0, radius
    )

    body = pymunk.Body(mass, moment)
    body.position = position

    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.75
    shape.friction = 1

    space.add(body, shape)

    return body, shape


def create_box(space, position, mass=1, width=80, height=80):
    moment = pymunk.moment_for_box(
        mass, (width, height)
    )

    body = pymunk.Body(mass, moment)
    body.position = position

    shape = pymunk.Poly.create_box(
        body, (width, height)
    )
    shape.elasticity = 0.75
    shape.friction = 1

    space.add(body, shape)

    return body, shape


def create_ground(space, width, y, radius=10):
    shape = pymunk.Segment(
        space.static_body,
        (0, y),
        (width, y),
        radius
    )

    shape.friction = 1
    shape.elasticity = 0.75

    space.add(shape)

    return shape
