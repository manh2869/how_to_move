import pygame
import pymunk
import physic
import DRAW

import player
import enemy

pygame.init()

W = 1200
H = 900
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("tank")

clock = pygame.time.Clock()
space = pymunk.Space()
space.damping = 1


player_body, player_shape, barrel_shape_m = player.create_player(space)

enemy_body, enemy_shape, barrel_shape_e = enemy.create_enemy(space)


physic.create_ground(space, W, H)
running = True
speed = 200


bullet = []
while running:
    dt = clock.tick(120) / 1000.0
    screen.fill((30, 30, 30))
    running = physic.shoot(space, screen, player_body, bullet, 25, running)

    player.player_move(player_body, speed, dt)
    player.draw_player(screen, player_body, player_shape, barrel_shape_m, BLUE)

    enemy.draw_enemy(screen, enemy_body, enemy_shape, barrel_shape_e, RED)

    DRAW.draw_bound(screen, W, H)
    DRAW.draw_grid(screen, W, H, 50)
    DRAW.draw_maze(screen, space)
    space.step(dt)
    pygame.display.flip()

pygame.quit()
