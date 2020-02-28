import numpy as np
import pygame
import time


def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                pygame.draw.rect(screen, (0, 255, 255), (
                    2 * c * 5 + 1, 2 * r * 5 + 1, 8, 8))
                # pygame.draw.circle(self.screen, self.ALIVE_COLOR, (
                #     2 * c * self.CELL_RADIUS + self.CELL_RADIUS, 2 * r * self.CELL_RADIUS + self.CELL_RADIUS),
                #                    self.CELL_RADIUS, 0)
            else:
                pygame.draw.rect(screen, (0, 0, 0), (
                    2 * c * 5, 2 * r * 5, 10, 10))
    pygame.display.flip()
    return


def update_grid(grid):
    def update_cell(g, row, col):
        cell = g[row][col]
        count_neighbors = -cell
        for i in range(row - 1, row + 2):
            if not 0 <= i < len(g):
                continue
            for j in range(col - 1, col + 2):
                if not 0 <= j < len(g[0]):
                    continue
                # count_neighbors += self.grid_last[i%(self.rows)][j%(self.cols)]
                count_neighbors += g[i][j]
        if cell == 1:
            if count_neighbors == 2 or count_neighbors == 3:
                return 1
            else:
                return 0
        if cell == 0:
            if count_neighbors == 3:
                return 1
            else:
                return 0

    grid_last = grid
    grid = [[update_cell(grid_last, r, c) for c in range(len(grid_last[0]))] for r in range(len(grid_last))]
    return grid


glider_gun = \
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

X = np.zeros((50, 70))
X[1:10, 1:37] = glider_gun

size = np.shape(X)[0] * 10, np.shape(X)[1] * 10
screen = pygame.display.set_mode(size)
print_grid(X)

while True:
    X = update_grid(X)
    print_grid(X)
    time.sleep(0.1)
