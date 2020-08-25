import pygame
import sys
from game_window import *
from button import *

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
        self.buttons = self.make_buttons()
        self.state = 'setting'

# ----------------------------SETTING---------------------------------------------
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
                else:
                    for button in self.buttons:
                        button.click()

    def update_gen(self):
        self.game_window.update()
        for button in self.buttons:
            mouse_position = pygame.mouse.get_pos()
            button.update(mouse_position)

    def draw(self):
        # fills screen with color
        self.window.fill(BACKGROUND)
        for button in self.buttons:
            button.draw()
        self.game_window.draw()

# -----------------------------RUNNING---------------------------------------------
    def running_get_events(self):
        # loops through event queue
        for event in pygame.event.get():
            # event is user clicking thw windows x button
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self.mouse_on_grid(mouse_position):
                    self.click_cell(mouse_position)
                else:
                    for button in self.buttons:
                        button.click()

    def running_update_gen(self):
        self.game_window.update()
        for button in self.buttons:
            mouse_position = pygame.mouse.get_pos()
            button.update(mouse_position)
        self.game_window.evaluate()

    def running_draw(self):
        # fills screen with color
        self.window.fill(BACKGROUND)
        for button in self.buttons:
            button.draw()
        self.game_window.draw()

# ------------------------------------PAUSED--------------------------------------
    def paused_get_events(self):
        # loops through event queue
        for event in pygame.event.get():
            # event is user clicking thw windows x button
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if self.mouse_on_grid(mouse_position):
                    self.click_cell(mouse_position)
                else:
                    for button in self.buttons:
                        button.click()

    def paused_update_gen(self):
        self.game_window.update()

        for button in self.buttons:
            mouse_position = pygame.mouse.get_pos()
            button.update(mouse_position)

    def paused_draw(self):
        # fills screen with color
        self.window.fill(BACKGROUND)
        for button in self.buttons:
            button.draw()
        self.game_window.draw()

# --------------------FUNCTIONS-------------------------------

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

    def make_buttons(self):
        buttons = []
        buttons.append(Button(self.window, WIDTH//5-50, 150, 100, 30, text='START',
                              color=(255, 255, 255), hover_color=(200, 200, 200), function=self.run_game))
        buttons.append(Button(self.window, WIDTH//2-50, 150, 100, 30, text='STOP',
                              color=(255, 255, 255), hover_color=(200, 200, 200), function=self.pause_game))
        buttons.append(Button(self.window, WIDTH//1.25-50, 150, 100, 30, text='RESET',
                              color=(255, 255, 255), hover_color=(200, 200, 200), function=self.reset_grid))
        return buttons

    def run_game(self):
        self.state = 'running'

    def pause_game(self):
        self.state = 'paused'

    def reset_grid(self):
        self.state = 'setting'
        self.game_window.reset_grid()

     # MAIN GAME LOOP

    def game_loop(self):

        while self.running:
            mouse_position = pygame.mouse.get_pos()
            if self.state == 'setting':
                self.get_events()
                # update contents of the display
                self.update_gen()
                self.draw()
            elif self.state == 'running':
                self.running_get_events()
                # update contents of the display
                self.running_update_gen()
                self.running_draw()
            elif self.state == 'paused':
                self.paused_get_events()
                # update contents of the display
                self.paused_update_gen()
                self.paused_draw()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = GameofLife()
    game.game_loop()
