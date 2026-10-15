import csv

FILE_NAME = "tank_data.csv"


def create_csv():
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "vx",
                "vy",
                "speed_t",
                "distance",
                "hit",
            ]
        )


def make_state(tank_body, target_body, vx, vy, speed):
    tx, ty = tank_body.position
    gx, gy = target_body.position
    dx, dy = gx - tx, gy - ty
    dist = (dx**2 + dy**2) ** 0.5

    return [round(v, 1) for v in (vx, vy, speed, dist)]


def save_data(state, hit):
    with open(FILE_NAME, "a", newline="") as file:
        csv.writer(file).writerow(state + [hit])
