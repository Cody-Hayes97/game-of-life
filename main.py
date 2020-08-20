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
# background color
BACKGROUND = (25, 55, 255)
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
        self.game_window = GameWindow(self.window, 80, 180)

    def get_events(self):
        # loops through event queue
        for event in pygame.event.get():
            # event is user clicking thw windows x button
            if event.type == pygame.QUIT:
                self.running = False

    def update_gen(self):
        self.game_window.update()

    def draw(self):
        self.window.fill(BACKGROUND)
        self.game_window.draw()
        # fills screen with color

 # MAIN GAME LOOP

    def game_loop(self):

        while self.running:
            self.get_events()
            # update contents of the display
            self.update_gen()
            self.draw()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = GameofLife()
    game.game_loop()
