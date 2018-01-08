import pygame
import time
import random
import sys

from breakout.ball import Ball
from breakout.paddle import Paddle



def handle_objects(movables, delta):
    [o.move(delta) for o in movables]

    for o in movables:
        for t in movables:
            if o.test_collision(t):
                o.resolve_collision(t.rect, 3)


def run():
    dt = 1 / 60
    random.seed(time.time())
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    ball = Ball(screen, x=width / 2, y=height / 2)
    paddle = Paddle(screen, width / 2, y=height - 100, color=pygame.Color('grey'))

    movables = [ball, paddle]

    current_time = time.time()
    while True:

        new_time = time.time()
        frame_time = new_time - current_time
        current_time = new_time

        # Check through the list of events that are in the queue
        for event in pygame.event.get():
            # If the event type is quit, break the loop
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Semi-fixed timestep
        while frame_time > 0.0:
            delta = min(frame_time, dt)
            handle_objects(movables, delta)
            frame_time -= delta

        screen.fill(pygame.Color('black'))
        # Things to render is put here
        ball.render()
        paddle.render()
        pygame.display.flip()


if __name__ == '__main__':
    run()
