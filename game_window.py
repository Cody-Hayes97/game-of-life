import pygame
from cell_class import *
vec = pygame.math.Vector2

CELL_SIZE = 10


class GameWindow:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = vec(x, y)
        self.width, self.height = 650, 650
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.init_grids()

    def init_grids(self):
        self.num_cols = 10
        self.num_rows = 10
        # self.num_cols = int(self.width / CELL_SIZE)
        # self.num_rows = int(self.height / CELL_SIZE)
        self.grid = [[Cell(self.image, x, y) for x in range(self.num_cols)]
                     for y in range(self.num_rows)]

    def update(self):
        # inspect the current active gen
        # update the inactive grid to store next gen
        # swap out the active grid
        self.rect.topleft = self.position
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((255, 255, 255))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.position.x, self.position.y))
        pygame.display.flip()
