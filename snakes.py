# Example file showing a basic pygame "game loop"
import pygame
import random
from enum import Enum

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WIDTH = 800
HEIGHT = 800
BLOCK_SIZE = 20
TIME_PER_FRAME = 250  # Time in ms
MOVE_SNAKE = pygame.event.custom_type()


class MovementDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


MOVEMENT_DIRECTION = MovementDirection(4)
grid = []
snake = []


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            grid.append(rect)
            pygame.draw.rect(screen, 'white', rect, 1)


def init_snake():
    x = 10 * BLOCK_SIZE
    y = 10 * BLOCK_SIZE
    rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    snake.append((rect, x, y))
    pygame.draw.rect(screen, 'red', rect)


def move_snake():
    global snake
    new_snake = []
    for block in snake:
        rect, x, y = block
        x_new = x
        y_new = y
        if MOVEMENT_DIRECTION == MovementDirection.RIGHT:
            x_new = x+BLOCK_SIZE
            y_new = y

        if MOVEMENT_DIRECTION == MovementDirection.LEFT:
            x_new = x-BLOCK_SIZE
            y_new = y

        if MOVEMENT_DIRECTION == MovementDirection.DOWN:
            x_new = x
            y_new = y+BLOCK_SIZE

        if MOVEMENT_DIRECTION == MovementDirection.UP:
            x_new = x
            y_new = y-BLOCK_SIZE

        new_rect = pygame.Rect(x_new, y_new, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, 'red', rect)

        new_snake.append((new_rect, x_new, y_new))
    snake = new_snake


def update_state():
    screen.fill("black")
    draw_grid()
    move_snake()


pygame.init()
pygame.time.set_timer(MOVE_SNAKE, TIME_PER_FRAME)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
init_snake()

# pygame setup
clock = pygame.time.Clock()
running = True
update_state()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOVE_SNAKE:
            update_state()
            print('Moving snake')
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                MOVEMENT_DIRECTION = MOVEMENT_DIRECTION.UP
            if keys[pygame.K_DOWN]:
                MOVEMENT_DIRECTION = MOVEMENT_DIRECTION.DOWN
            if keys[pygame.K_LEFT]:
                MOVEMENT_DIRECTION = MOVEMENT_DIRECTION.LEFT
            if keys[pygame.K_RIGHT]:
                MOVEMENT_DIRECTION = MOVEMENT_DIRECTION.RIGHT

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
