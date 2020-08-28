import pygame
from cell_class import *
import copy
vec = pygame.math.Vector2

CELL_SIZE = 20


class GameWindow:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = vec(x, y)
        self.width, self.height = 600, 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.init_grids()
        self.gen_count = 1

    def init_grids(self):
        # self.num_cols = 33
        # self.num_rows = 33
        self.num_cols = int(self.width / CELL_SIZE)
        self.num_rows = int(self.height / CELL_SIZE)
        self.grid = [[Cell(self.image, x, y) for x in range(self.num_cols)]
                     for y in range(self.num_rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbors(self.grid)

    def update(self):
        # inspect the current active gen
        # update the inactive grid to store next gen
        # swap out the active grid
        self.rect.topleft = self.position
        for row in self.grid:
            for cell in row:
                cell.update()

    def make_text(self):
        return f'Generation: {self.gen_count}'

    def draw(self):
        self.image.fill((255, 255, 255))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.position.x, self.position.y))
        pygame.display.flip()

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y) for x in range(self.num_cols)]
                     for y in range(self.num_rows)]

    def evaluate(self):
        new_grid = copy.copy(self.grid)

        for row in self.grid:
            for cell in row:
                cell.live_neighbors()

        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbors == 2 or cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True
                    if cell.alive_neighbors < 2:
                        new_grid[yidx][xidx].alive = False
                    if cell.alive_neighbors > 3:
                        new_grid[yidx][xidx].alive = False
                else:
                    if cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True
        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    new_grid[yidx][xidx].set_color()
        self.gen_count += 1
        self.grid = new_grid
