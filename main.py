import pygame
import sys
from game_window import *
from button import *
from text import *
import time

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
        self.state = 'setting'
        self.frame_count = 0

        self.buttons = self.make_buttons()
        self.fps = 60


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
        if self.frame_count % (self.fps//10) == 0:
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
        buttons.append(Button(self.window, WIDTH//3-50, 150, 100, 30, text='STOP',
                              color=(255, 255, 255), hover_color=(200, 200, 200), function=self.pause_game))
        buttons.append(Button(self.window, WIDTH//2-77, 150, 100, 30, text='RESET',
                              color=(255, 255, 255), hover_color=(200, 200, 200), function=self.reset_grid))
        buttons.append(Button(self.window, WIDTH//1.5-77, 150, 70, 30, text='SLOW',
                              color=(237, 245, 88), hover_color=(121, 128, 0), function=self.make_slow))
        buttons.append(Button(self.window, WIDTH//1.5, 150, 70, 30, text='FAST',
                              color=(237, 245, 88), hover_color=(121, 128, 0), function=self.make_fast))
        # -----------------------TITLE-------------------------------------------
        buttons.append(Button(self.window, WIDTH//2-150, -10, 300, 50, text="CONWAY'S GAME OF LIFE", border_color=(153, 204, 255),
                              color=(153, 204, 255), hover_color=(153, 204, 255)))
        #   ---------Generation DISPLAY-------------------------------------
        # buttons.append(Button(self.window, 450, 140, 200, 50, text=self.gen_text, border_color=(153, 204, 255),
        #                       color=(153, 204, 255), hover_color=(153, 204, 255)))
        #   -----------------------RULES-------------------------------
        buttons.append(Button(self.window, WIDTH//2-350, 40, 700, 30, text="Any live cell with fewer than two live neighbours dies, as if by underpopulation.", border_color=(153, 204, 255),
                              color=(153, 204, 255), hover_color=(153, 204, 255), text_size=16))
        buttons.append(Button(self.window, WIDTH//2-350, 65, 700, 30, text="Any live cell with two or three live neighbours lives on to the next generation.", border_color=(153, 204, 255),
                              color=(153, 204, 255), hover_color=(153, 204, 255), text_size=16))
        buttons.append(Button(self.window, WIDTH//2-350, 90, 700, 30, text="Any live cell with more than three live neighbours dies, as if by overpopulation.", border_color=(153, 204, 255),
                              color=(153, 204, 255), hover_color=(153, 204, 255), text_size=16))
        buttons.append(Button(self.window, WIDTH//2-400, 115, 800, 30, text="Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.", border_color=(153, 204, 255),
                              color=(153, 204, 255), hover_color=(153, 204, 255), text_size=16))
        return buttons

    def draw_gen(self):
        font = pygame.font.SysFont(None, 50)
        text = font.render(self.game_window.make_text(), True, ALIVE)
        self.window.blit(text, [400, 10])
        pygame.display.update()

    def run_game(self):
        self.state = 'running'

    def pause_game(self):
        self.state = 'paused'

    def reset_grid(self):
        self.state = 'setting'
        self.game_window.reset_grid()

    def make_slow(self):
        self.fps = 120

    def make_fast(self):
        self.fps = 10

     # MAIN GAME LOOP

    def game_loop(self):
        self.draw_gen()

        while self.running:
            self.frame_count += 1
            # print(self.fps)
            mouse_position = pygame.mouse.get_pos()
            if self.state == 'setting':

                self.get_events()
                # update contents of the display
                self.update_gen()
                self.draw()
                self.draw_gen()
            elif self.state == 'running':
                self.running_get_events()
                # update contents of the display
                self.running_update_gen()
                self.running_draw()
                self.draw_gen()
            elif self.state == 'paused':
                self.paused_get_events()
                # update contents of the display
                self.paused_update_gen()
                self.paused_draw()
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    game = GameofLife()
    game.game_loop()
