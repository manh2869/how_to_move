import csv
FILE_NAME = "tank_data.csv"


def create_csv():
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "tank_x",
                "tank_y",
                "target_x",
                "target_y",
                "dx",
                "dy",
                "distance",
                "angle",
                "hit",
            ]
        )


def save_data(tank_body, target_body, hit):
    tank_x = int(tank_body.position.x)
    tank_y = int(tank_body.position.y)

    target_x = int(target_body.position.x)
    target_y = int(target_body.position.y)

    dx = int(target_x - tank_x)
    dy = int(target_y - tank_y)

    distance = int((dx**2 + dy**2) ** 0.5)

    angle = int(tank_body.angle)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [tank_x, tank_y, target_x, target_y, dx, dy, distance, angle, hit]
        )
