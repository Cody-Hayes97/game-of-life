import pygame
vec = pygame.math.Vector2


class Button:
    def __init__(self, surface, x, y, width, height, state='', id='', function=0, color=(255, 255, 255), hover_color=(255, 255, 255), border=True, border_width=2, border_color=(0, 0, 0), text='', font_name='arial', text_size=20, text_color=(0, 0, 0), bold_text=False):
        self.x = x
        self.y = y
        self.position = vec(x, y)
        self.width = width
        self.height = height
        self.surface = surface
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.state = state
        self.id = id
        self.function = function
        self.color = color
        self.hover_color = hover_color
        self.border = border
        self.border_width = border_width
        self.border_color = border_color
        self.text = text
        self.font_name = font_name
        self.text_size = text_size
        self.text_color = text_color
        self.bold_text = bold_text
        self.hovered = False

    def update(self, pos, game_state=''):
        if self.mouse_hovering(pos):
            self.hovered = True
        else:
            self.hovered = False

    def draw(self):
        if self.border:
            self.image.fill(self.border_color)
            if self.hovered:
                pygame.draw.rect(self.image, self.hover_color, (self.border_width, self.border_width,
                                                                self.width-(self.border_width*2), self.height-(self.border_width*2)))
            else:
                pygame.draw.rect(self.image, self.color, (self.border_width, self.border_width,
                                                          self.width-(self.border_width*2), self.height-(self.border_width*2)))
        else:
            self.image.fill(self.color)
        if len(self.text) > 0:
            self.show_text()
        self.surface.blit(self.image, self.position)

    def show_text(self):
        font = pygame.font.SysFont(
            self.font_name, self.text_size, bold=self.bold_text)
        text = font.render(self.text, False, self.text_color)
        size = text.get_size()
        x, y = self.width//2 - (size[0]//2), self.height//2-(size[1]//2)
        pos = vec(x, y)
        self.image.blit(text, pos)

    def mouse_hovering(self, mouse_position):
        if mouse_position[0] > self.position[0] and mouse_position[0] < self.position[0]+self.width:
            if mouse_position[1] > self.position[1] and mouse_position[1] < self.position[1]+self.height:
                return True
        else:
            return False

    def click(self):
        if self.function != 0 and self.hovered:
            self.function()
