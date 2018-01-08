import pygame
from breakout.object import Object
from breakout.object_types import object_types


class Block(Object):
    def __init__(self, screen, x, y, width, height, color=pygame.Color("green")):
        Object.__init__(self, x, y, width, height, screen)
        self.color = color
        self.hitpoints = 1

    def resolve_collision(self, other, type):
        if type == object_types["ball"]:
            pass


