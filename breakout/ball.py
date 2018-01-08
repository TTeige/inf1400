import pygame
from breakout.movable import Movable
from breakout.object_types import object_types


class Ball(Movable):
    def __init__(self, screen, radius=10, color=pygame.Color('grey'), x=0, y=0):
        Movable.__init__(self, x, y, radius, radius, screen)
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.angle = 0
        # self.velocity = [random.randint(1, 100), 400]
        self.velocity = [100, 400]
        self.type = object_types["ball"]

    def render(self):
        self.rect = pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, dt):
        self.y += self.velocity[1] * dt
        self.x += self.velocity[0] * dt
        self.screen_bound()

    def screen_bound(self):
        if self.y + self.radius <= 0:
            self.y = 0 + self.radius
            self.velocity[1] *= -1

        if self.x + self.radius <= 0:
            self.x = self.radius
            self.velocity[0] *= -1
        if self.x + self.radius >= self.screen.get_width():
            self.x = self.screen.get_width() - self.radius
            self.velocity[0] *= -1

    def resolve_collision(self, other, type):
        if self.velocity[1] > 0:
            self.y = other.y - self.radius
        else:
            self.y = other.y + other.h + self.radius

        if type == object_types["paddle"]:
            pass
        # hyp = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        #
        # self.angle = math.cos(self.velocity[0] / hyp)



        self.velocity[1] *= -1
