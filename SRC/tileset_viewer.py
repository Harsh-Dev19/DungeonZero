
import pygame
import os
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DUNGEON ZERO - Tileset Viewer")

clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TILE_PATH = os.path.join(BASE_DIR, "assets", "tiles", "Floors_Tiles.png")

tileset = pygame.image.load(TILE_PATH).convert_alpha()

# Enlarge the image without blurring pixel art
zoom = 1.5
display_tileset = pygame.transform.scale_by(tileset, zoom)

font = pygame.font.SysFont("arial", 22)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 25))

    screen.blit(display_tileset, (20, 50))

    label = font.render("FLOOR TILESET", True, (230, 220, 190))
    screen.blit(label, (20, 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
