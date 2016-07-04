import pygame
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/boom.png").convert_alpha()
        self.rect = self.image.get_rect(center=(200, 250))
        self.lives = 3

        self.change_x = 0
        self.change_y = 0



    def update(self, platforms):
        self.calc_grav()

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y +=self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0





    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height



    def jump(self, platforms):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

    def subtract_lives(self):
        if self.lives > 0:
            self.lives -= 1

    def get_lives(self):
        return self.lives

    def set_lives(self, lives_count):
        self.lives = lives_count

