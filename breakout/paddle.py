import pygame

from breakout.movable import Movable
from breakout.object_types import object_types


class Paddle(Movable):
    def __init__(self, screen, x, y, width=300, height=20, color=pygame.Color('blue')):
        Movable.__init__(self, x, y, width, height, screen)
        self.color = color
        self.type = object_types["paddle"]

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self, dt):
        self.rect.x = pygame.mouse.get_pos()[0] - (self.rect.w / 2)
        if self.rect.x + self.rect.w > self.screen.get_width():
            self.rect.x = self.screen.get_width() - self.rect.w
        if self.rect.x < 0:
            self.rect.x = 0

    def test_collision(self, other):
        return self.rect.colliderect(other)

    def resolve_collision(self, other, type):
        pass

