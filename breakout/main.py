import os
import pygame
import time
import random
import sys

from breakout.ball import Ball
from breakout.block import Block
from breakout.paddle import Paddle


def run():
    dt = 1 / 60
    random.seed(time.time())
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    ball = Ball(screen, x=width / 2, y=height / 2)
    paddle = Paddle(screen, width / 2, y=height - 100, color=pygame.Color('grey'))
    balls = [ball]

    level = []
    with open(os.path.join("levels", "lvl1")) as f:
        defines = f.readline()
        defines = defines.split(" ")
        w, h = int(defines[0]), int(defines[1])
        y_offset = 10
        for row in f:
            x_offset = 0
            s = list(row)
            for c in s:
                if c == "-":
                    x_offset += w
                elif c == "b":
                    level.append(Block(screen, x_offset, y_offset, w, h))
                    x_offset += w
            y_offset += w

    all_objects = [ball, paddle]
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
            [i.update(delta) for i in all_objects]
            [b.update(delta) for b in level]

            for ball in balls:
                if ball.test_collision(paddle):
                    ball.resolve_collision(paddle)
                for block in level:
                    if ball.test_collision(block):
                        ball.resolve_collision(block)
                        block.resolve_collision(ball)
                        break

            frame_time -= delta
            for b in level:
                if b.hitpoints <= 0:
                    level.remove(b)
                    print(b)

        screen.fill(pygame.Color('black'))
        # Things to render is put here
        [i.render() for i in all_objects]
        [i.render() for i in level]
        pygame.display.flip()


if __name__ == '__main__':
    run()
