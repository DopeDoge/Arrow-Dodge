import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect(center=(x, y))
        ##self.image.fill(0,0,0)