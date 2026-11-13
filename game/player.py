import pygame
from config import COLORS, WIDTH, HEIGHT

class Player:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)
        self.speed = 245
        self.radius = 15
        self.health = 100
        self.rect = pygame.Rect(0, 0, 30, 30)
        self._sync_rect()

    def _sync_rect(self):
        self.rect.center = (int(self.x), int(self.y))

    def update(self, keys, dt, obstacles):
        dx = int(keys[pygame.K_d] or keys[pygame.K_RIGHT]) - int(keys[pygame.K_a] or keys[pygame.K_LEFT])
        dy = int(keys[pygame.K_s] or keys[pygame.K_DOWN]) - int(keys[pygame.K_w] or keys[pygame.K_UP])
        if dx and dy:
            dx *= 0.7071
            dy *= 0.7071

        old_x, old_y = self.x, self.y
        self.x += dx * self.speed * dt
        self._sync_rect()
        if self._collides(obstacles):
            self.x = old_x
            self._sync_rect()

        old_y = self.y
        self.y += dy * self.speed * dt
        self._sync_rect()
        if self._collides(obstacles):
            self.y = old_y
            self._sync_rect()

        self.x = max(18, min(WIDTH - 18, self.x))
        self.y = max(82, min(HEIGHT - 18, self.y))
        self._sync_rect()

    def _collides(self, obstacles):
        return any(self.rect.colliderect(o) for o in obstacles)

    def draw(self, surface):
        pygame.draw.circle(surface, (20, 80, 100), (int(self.x), int(self.y)), 22)
        pygame.draw.circle(surface, COLORS["mint"], (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, (230, 255, 255), (int(self.x - 4), int(self.y - 4)), 4)
