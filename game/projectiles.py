import pygame
from config import COLORS

class Projectile:
    def __init__(self, x, y, dx, dy, owner):
        self.x, self.y = float(x), float(y)
        self.dx, self.dy = dx, dy
        self.owner = owner
        self.speed = 510 if owner == "player" else 285
        self.rect = pygame.Rect(int(x), int(y), 10, 10)

    def update(self, dt):
        self.x += self.dx * self.speed * dt
        self.y += self.dy * self.speed * dt
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, surface):
        color = COLORS["yellow"] if self.owner == "player" else COLORS["red"]
        pygame.draw.circle(surface, color, self.rect.center, 5)
        pygame.draw.circle(surface, (255, 255, 230), self.rect.center, 2)
