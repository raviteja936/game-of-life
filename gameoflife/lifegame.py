import pygame
import random
import time
import sys


class LifeGame:

    def __init__(self, width=800, height=600, cell_size=10, fps=5, alive_color=(0, 255, 255), dead_color=(0, 0, 0)):
        """
        Initialize global parameters, grids, event handling flags
        :param width: width of game window
        :param height: height of game window
        :param cell_size: cell resolution
        :param fps: desired fps. -1 for max fps
        :param alive_color: RGB tuple for alive cell color
        :param dead_color: RGB tuple for dead  cell color
        """
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.DEAD_COLOR = dead_color
        self.ALIVE_COLOR = alive_color
        self.CELL_SIZE = cell_size
        self.fps = fps
        self.frame_time = int(1000 / self.fps)
        self.rows = int(self.height / self.CELL_SIZE)
        self.cols = int(self.width / self.CELL_SIZE)

        self.grid_last = self.init_grid(0)
        self.grid_curr = self.init_grid()

        self.paused = False
        self.quit = False

    def init_grid(self, val=None):
        """
        Creates and initializes a grid
        :param val: value with which the grid needs to be initialized
        :return: grid
        """
        if val is not None:
            grid = [[val for c in range(self.cols)] for r in range(self.rows)]
        else:
            grid = [[random.randint(0, 1) for c in range(self.cols)] for r in range(self.rows)]
        return grid

    def update_grid(self):
        """
        Copies the current grid to last grid. Updates current grid using rules in update_cell function
        :return:
        """
        def update_cell(row, col):
            cell = self.grid_last[row][col]
            count_neighbors = -cell
            for i in range(row - 1, row + 2):
                if not 0 <= i < self.rows:
                    continue
                for j in range(col - 1, col + 2):
                    if not 0 <= j < self.cols:
                        continue
                    count_neighbors += self.grid_last[i][j]
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

        self.grid_last = self.grid_curr
        self.grid_curr = self.init_grid(0)
        self.grid_curr = [[update_cell(r, c) for c in range(self.cols)] for r in range(self.rows)]

    def print_grid(self):
        """
        Prints the current grid to screen
        :return:
        """
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid_curr[r][c] == 1:
                    pygame.draw.rect(self.screen, self.ALIVE_COLOR, (
                        c * self.CELL_SIZE + 1, r * self.CELL_SIZE + 1, self.CELL_SIZE-2, self.CELL_SIZE-2))
                else:
                    pygame.draw.rect(self.screen, self.DEAD_COLOR, (
                        c * self.CELL_SIZE, r * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        pygame.display.flip()
        return

    def time_delay(self, start_time):
        """
        Delays time to set the desired FPS
        :param start_time: Input time at which the function has been called
        :return:
        """
        sleep_time = self.frame_time - (int(round(time.time() * 1000)) - start_time)
        if sleep_time > 0:
            time.sleep(sleep_time / 1000)
        return

    def event_handler(self):
        """
        Handles key presses
        q -- quit game
        r -- re-initialize to random cells
        s -- pause/play
        e -- next frame
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("key pressed")
                if event.unicode == "s":
                    print("Toggling pause.")
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif event.unicode == "r":
                    print("Randomizing grid.")
                    self.grid_curr = self.init_grid()
                elif event.unicode == "q":
                    print("Quitting game")
                    self.quit = True
                elif event.unicode == "e":
                    print("Next frame")
                    self.update_grid()
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        """
        Run the game
        :return:
        """
        while True:
            start_time = int(round(time.time() * 1000))
            self.print_grid()
            self.event_handler()
            if self.quit:
                return
            if not self.paused:
                self.update_grid()
                self.time_delay(start_time)


if __name__ == "__main__":
    game = LifeGame()
    game.run_game()
