import pygame
from pygame.sprite import Sprite

class BaseBullet(Sprite):
    def __init__(self, ship_game, x, y, direction):
        super().__init__()
        self.screen = ship_game.screen
        self.ajustes = ship_game.ajustes
        self.color = self.ajustes.color_municion
        self.rect = pygame.Rect(x, y, self.ajustes.width_municion, self.ajustes.height_municion)
        self.y = float(self.rect.y)
        self.direction = direction  # Define si la bala sube o baja

    def update(self):
        # Actualiza la posición de la bala según su dirección
        self.y += self.ajustes.vel_municion * self.direction
        self.rect.y = self.y
        # Eliminar si sale de los límites de la pantalla
        if self.rect.bottom <= 0 or self.rect.top >= self.ajustes.height:
            self.kill()

    def draw_municion(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet(BaseBullet):
    def __init__(self, ship_game):
        super().__init__(ship_game, ship_game.ally.rect.midtop[0], ship_game.ally.rect.midtop[1], -1)

class EnemyBullet(BaseBullet):
    def __init__(self, ship_game, x, y):
        super().__init__(ship_game, x, y, 1)
