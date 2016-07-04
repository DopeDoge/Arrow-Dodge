import pygame
import random
random_place = random.randrange(50,431)

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/Arrow.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x -= 5
        if self.rect.x <= 0:
            random_place = random.randrange(50,431)
            self.rect.x = 640
            self.rect.y = random_place
    def collision(self):
        self.rect.y = 0
