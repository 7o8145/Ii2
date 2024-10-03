#!/usr/bin/python3

import pygame
import random

# Настройки игры
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Цвета
COLORS = [
    (0, 0, 0),  # Черный
    (255, 0, 0),  # Красный
    (0, 255, 0),  # Зелёный
    (0, 0, 255),  # Синий
    (255, 255, 0),  # Жёлтый
    (255, 165, 0),  # Оранжевый
    (128, 0, 128),  # Пурпурный
]

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.current_pos = (0, GRID_WIDTH // 2 - 1)

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape) + 1]
        return shape, color

    def rotate_piece(self):
        self.current_piece[0] = [list(row) for row in zip(*self.current_piece[0][::-1])]

    def valid_move(self, offset=(0, 0)):
        shape, _ = self.current_piece
        for i, row in enumerate(shape):
            for j, val in enumerate(row):
                if val:
                    new_x = self.current_pos[0] + i + offset[0]
                    new_y = self.current_pos[1] + j + offset[1]
                    if new_x < 0 or new_x >= GRID_HEIGHT or new_y < 0 or new_y >= GRID_WIDTH or \
                            (new_x >= 0 and self.grid[new_x][new_y]):
                        return False
        return True

    def fix_piece(self):
        shape, color = self.current_piece
        for i, row in enumerate(shape):
            for j, val in enumerate(row):
                if val:
                    self.grid[self.current_pos[0] + i][self.current_pos[1] + j] = color
        self.clear_lines()
        self.current_piece = self.new_piece()
        self.current_pos = (0, GRID_WIDTH // 2 - 1)

    def clear_lines(self):
        self.grid = [row for row in self.grid if any(val == 0 for val in row)]
        while len(self.grid) < GRID_HEIGHT:
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])

    def drop_piece(self):
        if self.valid_move((1, 0)):
            self.current_pos = (self.current_pos[0] + 1, self.current_pos[1])
        else:
            self.fix_piece()

    def move_piece(self, direction):
        if self.valid_move((0, direction)):
            self.current_pos = (self.current_pos[0], self.current_pos[1] + direction)

    def get_grid(self):
        grid_copy = [row.copy() for row in self.grid]
        shape, color = self.current_piece
        for i, row in enumerate(shape):
            for j, val in enumerate(row):
                if val:
                    grid_copy[self.current_pos[0] + i][self.current_pos[1] + j] = color
        return grid_copy

def draw_grid(screen, grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            color = COLORS[val] if val else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(screen, (255, 255, 255), (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    tetris = Tetris()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move_piece(-1)
                if event.key == pygame.K_RIGHT:
                    tetris.move_piece(1)
                if event.key == pygame.K_DOWN:
                    tetris.drop_piece()
                if event.key == pygame.K_UP:
                    tetris.rotate_piece()

        tetris.drop_piece()
        screen.fill((0, 0, 0))
        draw_grid(screen, tetris.get_grid())
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()