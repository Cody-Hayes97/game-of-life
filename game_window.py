import pygame
vec = pygame.math.Vector2


class GameWindow:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.position = vec(x, y)
        self.width, self.height = 650, 650
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = self.position

    def draw(self):
        self.image.fill((100, 100, 100))
        self.screen.blit(self.image, (self.position.x, self.position.y))