import pygame
vec = pygame.math.Vector2


class Text:
    def __init__(self, surface, x, y, font_name, text_size, text, text_color=(0, 0, 0)):
        self.surface = surface
        self.font_name = font_name
        self.text_size = text_size
        self.text = text
        self.text_color = text_color
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((50, 50))

    def show_text(self):
        font = pygame.font.SysFont(
            self.font_name, self.text_size)
        text = font.render(self.text, False, self.text_color)
        size = text.get_size()
        x, y = self.width//2 - (size[0]//2), self.height//2-(size[1]//2)
        pos = vec(x, y)
        self.image.blit(text, pos)
