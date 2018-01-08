import pygame


class Drawable:
    def __init__(self, screen):
        self.screen = screen

    def render(self):
        raise NotImplementedError(
            "Class %s doesn't implement render(), required for drawable objects" % (self.__class__.__name__))
