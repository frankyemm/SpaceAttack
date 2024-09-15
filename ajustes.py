import pygame
from random import randint

class Ajustes:
    def __init__(self):
        #Variables para la pantalla del juego
        self.width = 840
        self.height = 500
        self.background = 'fotos/fondo.jpg'
        
        #Variables menu principal
        self.menu_background = pygame.image.load('fotos/menubackground.jpeg')
        self.menu_background = pygame.transform.scale(self.menu_background, (self.width, self.height))
        
        #Variables para las balas
        self.vel_municion = 3
        self.width_municion = 3
        self.height_municion = 10
        self.color_municion = (0,201,255)
        self.limite_municion = 10
        self.sound = pygame.mixer.Sound('sonidos/laser.mp3')
        
        #Variables para el enemigo
        enemies = ('fotos/nave_enemiga1copy.bmp','fotos/nave_enemiga2copy.bmp','fotos/nave_enemiga3copy.bmp','fotos/nave_enemiga4copy.bmp')
        self.game_enemies = pygame.image.load(enemies[randint(0,3)])
        self.vel_enemies = 1.5
        self.shoot_rate = 1
        self.enemy_rate = 2
        self.vel_shot = 2
        self.explosion_sound = pygame.mixer.Sound('sonidos/explosion_enemies.mp3')
        self.explosion_pic = 'fotos/explosion.bmp'
        
        #Variables de bonificación
        self.lost_enemies = 10
        self.lives = 5
