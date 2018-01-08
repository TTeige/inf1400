import pygame

from breakout.drawable import Drawable


class Movable(Drawable):
    def __init__(self, x, y, width, height, screen):
        Drawable.__init__(self, screen)
        self.rect = pygame.Rect(x, y, width, height)

    def render(self):
        Drawable.render(self)

    def move(self, dt):
        pass

    def test_collision(self, other):
        if self == other:
            return False
        return self.rect.colliderect(other)

    def resolve_collision(self, other, type):
        pass