import pygame
import sys
from game_window import *


# GAME RULES
# -----------------------------------------------
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

WIDTH, HEIGHT = 800, 800
# Light blue
BACKGROUND = (153, 204, 255)
# black
ALIVE = (0, 0, 0)
FPS = 60


class GameofLife:
    def __init__(self):
        # initializes pygame
        pygame.init()
        # setting the dimension of the game screen
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        # clock ticks once per frame in miliseconds
        self.clock = pygame.time.Clock()
        self.game_window = GameWindow(self.window, 100, 200)

    def get_events(self):
        # loops through event queue
        for event in pygame.event.get():
            # event is user clicking thw windows x button
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self.mouse_on_grid(mouse_position):
                    self.click_cell(mouse_position)

    def update_gen(self):
        self.game_window.update()

    def draw(self):
        # fills screen with color
        self.window.fill(BACKGROUND)
        self.game_window.draw()

    def mouse_on_grid(self, pos):
        if pos[0] > 100 and pos[0] < WIDTH - 100:
            if pos[1] > 180 and pos[1] < HEIGHT:
                return True
        return False

    def click_cell(self, pos):
        grid_position = [pos[0]-100, pos[1]-200]
        grid_position[0] = grid_position[0] // 20
        grid_position[1] = grid_position[1] // 20
        if self.game_window.grid[grid_position[1]][grid_position[0]].alive:
            self.game_window.grid[grid_position[1]
                                  ][grid_position[0]].alive = False
        else:
            self.game_window.grid[grid_position[1]
                                  ][grid_position[0]].alive = True

     # MAIN GAME LOOP

    def game_loop(self):

        while self.running:
            self.get_events()
            # update contents of the display
            self.update_gen()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = GameofLife()
    game.game_loop()
