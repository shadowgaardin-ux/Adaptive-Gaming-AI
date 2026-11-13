import pygame
from config import WIDTH, HEIGHT, COLORS

def build_obstacles():
    # Hand-designed starter arena. Later this will be replaced/augmented by the level generator.
    blocks = [
        (250, 155, 115, 36), (430, 235, 42, 135), (630, 135, 130, 38),
        (790, 275, 42, 125), (300, 455, 140, 35), (575, 485, 42, 95),
        (890, 490, 100, 36), (165, 300, 40, 90)
    ]
    return [pygame.Rect(*b) for b in blocks]

def draw_arena(surface, obstacles):
    surface.fill(COLORS["background"])
    # subtle floor grid
    for x in range(0, WIDTH, 40):
        pygame.draw.line(surface, COLORS["grid"], (x, 62), (x, HEIGHT), 1)
    for y in range(62, HEIGHT, 40):
        pygame.draw.line(surface, COLORS["grid"], (0, y), (WIDTH, y), 1)
    # arena edge
    pygame.draw.rect(surface, (35, 76, 105), (8, 70, WIDTH - 16, HEIGHT - 78), 2, border_radius=8)
    for obstacle in obstacles:
        pygame.draw.rect(surface, (30, 53, 76), obstacle, border_radius=5)
        pygame.draw.rect(surface, COLORS["wall"], obstacle, 2, border_radius=5)
        pygame.draw.line(surface, (68, 94, 117), (obstacle.x + 6, obstacle.y + 6), (obstacle.right - 6, obstacle.y + 6), 2)
