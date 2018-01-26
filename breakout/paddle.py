import pygame

from breakout.object import Object
from breakout.object_types import object_types


class Paddle(Object):
    def __init__(self, screen, x, y, width=300, height=20, color=pygame.Color('blue')):
        Object.__init__(self, x, y, width, height, screen, object_types["paddle"])
        self.color = color

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.rect.x = pygame.mouse.get_pos()[0] - (self.rect.w / 2)
        if self.rect.x + self.rect.w > self.screen.get_width():
            self.rect.x = self.screen.get_width() - self.rect.w
        if self.rect.x < 0:
            self.rect.x = 0

    def test_collision(self, other):
        return self.rect.colliderect(other)

    def resolve_collision(self, other):
        pass

