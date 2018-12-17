import pygame
import time
from pygame.locals import *
import random
from random import randint


#jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('milos.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

#posição do jogador
    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -2)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 2)
        if pressed_keys[K_a]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(2, 0)

#não sair da tela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

#inimigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('dota.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = random.randint(1,2)
#movimentação do inimigo(eu acho)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((800, 600))
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 800)
player = Player()

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

#grupos de sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


#loops
running = True


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif(event.type == ADDENEMY):
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)



#prender na tela
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()


#atualizar a tela
    pygame.display.flip()

