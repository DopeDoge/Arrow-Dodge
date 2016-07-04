import pygame
import sys
from pygame.locals import *
from Player import Player
from Enemy import Enemy
from Platform import Platform

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load("images/Corridor.png").convert_alpha();
screen.blit(background, (0, 0))

pygame.display.set_caption('Game Base')
font = pygame.font.SysFont(None, 36)

player = Player()
enemy = Enemy(600, 350)
# width, height, x, y
p1 = Platform(SCREEN_WIDTH, 50, 320, 455)
p2 = Platform(SCREEN_WIDTH, 50, 320, 25)
p3 = Platform(160, 70, 400, 330)

enemy_group = pygame.sprite.Group()
all_group = pygame.sprite.Group()
platforms = pygame.sprite.Group()
all_group.add(player)
all_group.add(enemy)
enemy_group.add(enemy)
platforms.add(p1)
platforms.add(p2)
platforms.add(p3)
all_group.add(p1)
all_group.add(p2)
all_group.add(p3)


done = False
score = 0
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)
score_text = font.render('Score: %s' %(score), 1, (0, 0, 0))
score_rect = score_text.get_rect()
score_rect.topleft = (80,82)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_UP:
                player.jump(platforms)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()
    clock.tick(60)

    collide_list = pygame.sprite.spritecollide(player, enemy_group, False, collided = None)
    if len(collide_list) > 0:
        player.subtract_lives()
        for enemy in collide_list:
            enemy.collision()
    score += 10
    score_text = font.render('Score: %s' % (score), 1, (0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(score_text, score_rect)
    player.update(platforms)

    all_group.clear(screen, background)
    all_group.draw(screen)
    enemy.update()

    pygame.display.update()



##
##
##enemy_group = pygame.sprite.Group()
##enemy_group.add(enemy)
##
##all_group = pygame.sprite.Group()
##all_group.add(player)
##all_group.add(enemy)
##
##main_clock = pygame.time.Clock()
##
##direction =-1
##

##


##
##    keys = pygame.key.get_pressed()
##
##    if state == 0:
##
##        if keys[K_d]:
##            direction = 1
##        elif keys[K_a]:
##            direction = 0
##
##        else:
##            direction = -1
##

##

##
##        player.update(direction)
##        enemy.update()
##
##        all_group.clear(screen, background)
##
##        all_group.draw(screen)
##
##        if player.get_lives() <= 0:
##            state = 1
##
##    elif state == 1:
##
##        if keys[K_RETURN]:
##            score = 0
##            player.set_lives(3)
##            state = 0
##
##        instructions = font.render('Press Enter to play again.', 1, (0, 0, 0))
##        instructions_rect = score_rect
##        screen.blit(background, (0, 0))
##        screen.blit(instructions, instructions_rect)