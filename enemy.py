import pygame
from pygame.sprite import Sprite
from random import randint
from municion import EnemyBullet

class Enemy(Sprite):
    def __init__(self, ship_game):
        super().__init__()
        self.ship_game = ship_game
        self.ajustes = ship_game.ajustes
        self.screen = ship_game.screen
        self.image = self.ajustes.game_enemies
        self.rect = self.image.get_rect()

        screen_rect = self.screen.get_rect()
        self.rect.x = randint(0, screen_rect.width - self.rect.width)
        self.rect.y = randint(-100, -self.rect.height)
    
    def update(self):
        self.rect.y += self.ajustes.vel_enemies
    
    def enemy_shoot(self):
        new_shoot = EnemyBullet(self.ship_game, self.rect.centerx, self.rect.bottom)
        self.ship_game.enemiesBullet.add(new_shoot)
