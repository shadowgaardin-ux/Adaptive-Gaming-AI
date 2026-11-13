import pygame
import math
import random
from config import COLORS, WIDTH, HEIGHT

class Enemy:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)
        self.speed = 105
        self.health = 100
        self.rect = pygame.Rect(0, 0, 34, 34)
        self.last_shot = 0
        self._sync_rect()

    def _sync_rect(self):
        self.rect.center = (int(self.x), int(self.y))

    def update(self, player, dt, obstacles):
        dx, dy = player.x - self.x, player.y - self.y
        dist = max(1, math.hypot(dx, dy))
        # Starter opponent uses a simple pursuit rule; later we'll replace this with adaptive tactics.
        old_x, old_y = self.x, self.y
        self.x += dx / dist * self.speed * dt
        self._sync_rect()
        if any(self.rect.colliderect(o) for o in obstacles):
            self.x = old_x
            self._sync_rect()
        old_y = self.y
        self.y += dy / dist * self.speed * dt
        self._sync_rect()
        if any(self.rect.colliderect(o) for o in obstacles):
            self.y = old_y
            self._sync_rect()
        self.x = max(18, min(WIDTH - 18, self.x))
        self.y = max(82, min(HEIGHT - 18, self.y))
        self._sync_rect()

    def can_fire(self, now, player):
        return now - self.last_shot > 1300 and math.hypot(player.x - self.x, player.y - self.y) < 430

    def draw(self, surface):
        pygame.draw.circle(surface, (85, 25, 48), (int(self.x), int(self.y)), 24)
        pygame.draw.rect(surface, COLORS["red"], self.rect, border_radius=7)
        pygame.draw.rect(surface, (255, 210, 220), (self.rect.x + 9, self.rect.y + 9, 5, 5))
        pygame.draw.rect(surface, (255, 210, 220), (self.rect.x + 20, self.rect.y + 9, 5, 5))
        # Enemy health bar
        pygame.draw.rect(surface, (60, 25, 40), (self.rect.x - 2, self.rect.y - 10, 38, 5), border_radius=2)
        pygame.draw.rect(surface, COLORS["red"], (self.rect.x - 2, self.rect.y - 10, max(0, 38 * self.health / 100), 5), border_radius=2)
