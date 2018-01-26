import pygame

from breakout.drawable import Drawable


class Object(Drawable):
    def __init__(self, x, y, width, height, screen, object_type):
        Drawable.__init__(self, screen)
        self.rect = pygame.Rect(x, y, width, height)
        self.type = object_type

    def update(self, dt):
        raise NotImplementedError(
            "Class %s doesn't implement render(), required for drawable objects" % (self.__class__.__name__))

    def render(self):
        Drawable.render(self)

    def test_collision(self, other):
        if self == other:
            return False
        return self.rect.colliderect(other)

    def resolve_collision(self, other):
        raise NotImplementedError(
            "Class %s doesn't implement render(), required for drawable objects" % (self.__class__.__name__))