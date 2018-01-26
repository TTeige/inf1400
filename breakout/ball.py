import random

import pygame
import math
from breakout.object import Object
from breakout.object_types import object_types


class Ball(Object):
    def __init__(self, screen, radius=10, color=pygame.Color('grey'), x=0, y=0):
        Object.__init__(self, x, y, radius, radius, screen, object_types["ball"])
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = [random.randint(1, 100), 400]
        # self.velocity = [100, 400]
        self.type = object_types["ball"]

    def render(self):
        self.rect = pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self, dt):
        self.move(dt)

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

    def light_refraction_angle_update(self, other, direction):
        if self.velocity[1] > 0:
            self.y = other.rect.y - self.radius
        else:
            self.y = other.rect.y + other.rect.h + self.radius
        n1 = 1
        other_center = other.rect.x + other.rect.w / 2
        dist = math.fabs(self.x - other_center)
        norm_dist_w = dist / (other.rect.w / 2)
        n2 = 1 + norm_dist_w
        hyp = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        self.angle = math.cos(self.velocity[0] / hyp)
        new_angle = n2 / n1 * math.sin(self.angle)

        if self.x > other_center:
            new_vx = math.sin(new_angle) * self.velocity[1] * direction
        else:
            new_vx = math.sin(-new_angle) * self.velocity[1] * direction

        self.velocity[0] = new_vx
        self.velocity[1] *= -1

    def resolve_collision(self, other):
        if other.type == object_types["paddle"]:
            self.light_refraction_angle_update(other, 1)
        if other.type == object_types["block"]:
            self.light_refraction_angle_update(other, -1)
