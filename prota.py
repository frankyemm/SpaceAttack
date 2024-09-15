import pygame

class Shipp:
    def __init__(self,ship_game):
        self.screen = ship_game.screen
        self.screen_rect = ship_game.screen.get_rect()
        self.ally = pygame.image.load('fotos/nave_aliadacopy.bmp')
        self.rect = self.ally.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        #Controles de movimiento
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False    
    def blime(self):
        self.screen.blit(self.ally,self.rect)
    
    def update_move(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 4
        if self.move_left and self.rect.left > 0:
            self.rect.x -= 4
        if self.move_up and self.rect.top > 0:
            self.rect.y -= 4
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 4
    