import pygame
from breakout.object import Object
from breakout.object_types import object_types


class Block(Object):
    def __init__(self, screen, x, y, width, height, color=pygame.Color("green"), hitpoints=1):
        Object.__init__(self, x, y, width, height, screen, object_types["block"])
        self.color = color
        self.hitpoints = hitpoints

    def update(self, dt):
        if self.hitpoints == 0:
            return False

    def resolve_collision(self, other):
        if other.type == object_types["ball"]:
            self.hitpoints -= 1

    def render(self):
        if self.hitpoints > 0:
            pygame.draw.rect(self.screen, self.color, self.rect)

