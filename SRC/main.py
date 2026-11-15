
import pygame
import sys

from dungeon import Dungeon

# Initialize Pygame
pygame.init()

# Window settings
WIDTH = 1000
HEIGHT = 700
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DUNGEON ZERO")

clock = pygame.time.Clock()

dungeon = Dungeon()

# Colors
BACKGROUND = (18, 17, 22)
TEXT_COLOR = (210, 205, 190)

font = pygame.font.SysFont("arial", 32)

# Game loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dungeon.draw(screen)

    title = font.render("DUNGEON ZERO", True, TEXT_COLOR)
    screen.blit(
        title,
        title.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    )

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
