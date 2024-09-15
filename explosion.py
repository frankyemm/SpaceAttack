import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, ship_game, position):
        super().__init__()
        self.screen = ship_game.screen
        self.ajustes = ship_game.ajustes
        self.frames = []
        # Cargar fotogramas de la animación
        for i in range(1,6):  # Suponiendo que tienes 5 fotogramas para la explosión
            image = pygame.image.load(f'fotos/explosiones/explosion00{i}.bmp')
            self.frames.append(image)
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=position)
        self.animation_speed = 5  # Velocidad de cambio de fotogramas
        self.time_since_last_frame = 0

    def update(self):
        self.time_since_last_frame += self.ajustes.vel_enemies
        if self.time_since_last_frame >= self.animation_speed:
            self.time_since_last_frame = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
            else:
                self.kill()  # Eliminar explosión cuando la animación termine
