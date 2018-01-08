import pygame
import math
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

    def resolve_collision(self, other, other_type):
        if self.velocity[1] > 0:
            self.y = other.y - self.radius
        else:
            self.y = other.y + other.h + self.radius

        if other_type == object_types["paddle"]:
            n1 = 1
            other_center = other.x + other.w / 2
            dist = math.fabs(self.x - other_center)
            norm_dist_w = dist / (other.w / 2)
            n2 = 1 + norm_dist_w
            hyp = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
            self.angle = math.cos(self.velocity[0] / hyp)
            new_angle = n2 / n1 * math.sin(self.angle)

            if self.x > other_center:
                new_vx = math.sin(new_angle) * self.velocity[1]
            else:
                new_vx = math.sin(-new_angle) * self.velocity[1]

            self.velocity[0] = new_vx



        self.velocity[1] *= -1
