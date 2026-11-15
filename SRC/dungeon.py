import pygame
import os


title_size = 48

room_columns = 16
room_rows = 10

room_width = room_columns*title_size
room_height = room_rows*title_size

room_x = 104
room_y = 100

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

floor_path = os.path.join(
    base_dir,
    "assets",
    "tiles",
    "Floors_Tiles.png",
)

def load_assets():

    floor_sheet = pygame.image.load(
        floor_path
    ).convert_alpha()

    floor_title = floor_sheet.subsurface(
        pygame.Rect(260,0, title_size,title_size)
    ).copy()

    return floor_title

class Dungeon:

    def __init__(self):

        self.floor_tile = load_assets()

        self.wall_rects = []

        # Create collision boundaries.
        self.create_walls()

    def create_walls(self):

        self.wall_rects.clear()

        for col in range(room_columns):

            x = room_x + col * title_size

            # Top wall
            self.wall_rects.append(
                pygame.Rect(
                    x, room_y,
                    title_size, title_size
                )
            )

            # Bottom wall
            self.wall_rects.append(
                pygame.Rect(
                    x,
                    room_y + room_height - title_size,
                    title_size, title_size
                )
            )

        for row in range(1, room_rows - 1):

            y = room_y + row * title_size

            # Left wall
            self.wall_rects.append(
                pygame.Rect(
                    room_x, y,
                    title_size, title_size
                )
            )

            # Right wall
            self.wall_rects.append(
                pygame.Rect(
                    room_x + room_width - title_size,
                    y,
                    title_size, title_size
                )
            )

    # -----------------------------
    # DRAW DUNGEON
    # -----------------------------

    def draw(self, screen):

        screen.fill((12, 12, 17))

        # Draw floor tiles.
        for row in range(room_rows):

            for col in range(room_columns):

                x = room_x + col * title_size
                y = room_y + row * title_size

                screen.blit(
                    self.floor_tile,
                    (x, y)
                )

        # Draw temporary walls.
        for wall in self.wall_rects:

            pygame.draw.rect(
                screen,
                (30, 32, 39),
                wall
            )

            pygame.draw.rect(
                screen,
                (75, 80, 91),
                wall,
                2
            )

        # Room border.
        pygame.draw.rect(
            screen,
            (110, 110, 120),
            (
                room_x,
                room_y,
                room_width,
                room_height
            ),
            2
        )
