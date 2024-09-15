import pygame
import sys
from ajustes import Ajustes
from prota import Shipp
from municion import Bullet
from enemy import Enemy
from random import randint
from explosion import Explosion
from menu import MenuPrincipal

class Aliado():
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()
        self.screen = pygame.display.set_mode((self.ajustes.width, self.ajustes.height))
        self.background = pygame.image.load(self.ajustes.background)
        pygame.display.set_caption("Space Game")
        self.ally = Shipp(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemiesBullet = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.launch_enemies()
        self.points = 0
        self.health = self.ajustes.lives
        self.lost_enemies = self.ajustes.lost_enemies
    
    def launch_enemies(self):
        if len(self.enemies) < 0 or (len(self.enemies) < 3 and randint(1,100) <= self.ajustes.enemy_rate): 
            enemy = Enemy(self)
            self.enemies.add(enemy)
    
    def delete_enemies(self):
        for enemy in self.enemies.copy():
            if enemy.rect.bottom >= self.ajustes.height:
                self.enemies.remove(enemy)
                self.you_lost()
                self.lost_enemies -= 1
                self.launch_enemies()
    
    def update_enemies(self):
        self.enemies.update()
    
    def enemy_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets, self.enemies,True, True)
        if collision:
            self.ajustes.explosion_sound.play()
            for enemy in collision.values():
                explosion = Explosion(self, enemy[0].rect.center)
                self.explosions.add(explosion)
            self.points += 1
            self.lost_enemies += 1
    
    def ally_collision(self):
        collision_ship = pygame.sprite.spritecollide(self.ally, self.enemies, True)
        collision_enemy_bullet = pygame.sprite.spritecollide(self.ally, self.enemiesBullet, True)
        if len(collision_ship) !=0 or len(collision_enemy_bullet) != 0:
            self.ajustes.explosion_sound.play()
            self.health -= 1
            self.you_lost()
        
    def shoot_enemies(self):
        for enemy in self.enemies:
            if randint(1,100) <= self.ajustes.shoot_rate:
                enemy.enemy_shoot()
    
    def you_lost(self):
        if self.health <= 0 or self.lost_enemies < 0:
            sys.exit()            
    
    def update_screen(self):
        self.screen.blit(self.background,(0,0))
        self.ally.blime()
        for bullet in self.bullets.sprites():
            bullet.draw_municion()
        self.enemies.draw(self.screen)
        for enemybullet in self.enemiesBullet.sprites():
            enemybullet.draw_municion()
        self.explosions.draw(self.screen)
        self.score()
        self.healthy()
        self.enemies_loses()
        pygame.display.flip()
    
    def shoot(self):
        if len(self.bullets) < self.ajustes.limite_municion:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def delete_shoot(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    def eventos(self):
        #Aquí capturamos los eventos que suceden en nuestro teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ally.move_right = True

                elif event.key == pygame.K_LEFT:
                    self.ally.move_left = True

                elif event.key == pygame.K_UP:
                    self.ally.move_up = True

                elif event.key == pygame.K_DOWN:
                    self.ally.move_down = True
                
                elif event.key == pygame.K_SPACE:
                    self.ajustes.sound.play()
                    self.shoot()   

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ally.move_right = False

                if event.key == pygame.K_LEFT:
                    self.ally.move_left = False

                if event.key == pygame.K_UP:
                    self.ally.move_up = False

                if event.key == pygame.K_DOWN:
                    self.ally.move_down = False

    
    def run_game(self):
        while True:
            self.eventos()
            self.ally.update_move()
            self.bullets.update()
            self.shoot_enemies()
            self.enemy_collision()
            self.enemiesBullet.update()
            self.explosions.update()
            self.delete_shoot()
            self.launch_enemies()
            self.update_enemies()
            self.delete_enemies()
            self.ally_collision()
            self.update_screen()
            pygame.time.Clock().tick(60)
    
    def score(self):
        font = pygame.font.SysFont("Minecraftia-Regular", 30)
        text_surface = font.render(str(self.points), True, (255, 255, 255))
        rect_text = text_surface.get_rect()
        rect_text.midtop = (420, 20)
        self.screen.blit(text_surface, rect_text)
    
    def healthy(self):
        font = pygame.font.SysFont("Minecraftia-Regular", 30)
        text_surface = font.render(f"+ = {str(self.health)}", True, (255, 255, 255), (0,0,255))
        rect_text = text_surface.get_rect()
        rect_text.midtop = (75, 0)
        self.screen.blit(text_surface, rect_text)
        
    def enemies_loses(self):
        font = pygame.font.SysFont("Minecraftia-Regular", 30)
        text_surface = font.render(f"Lost enemies = {str(self.lost_enemies)}", True, (255, 255, 255), (255,0,0))
        rect_text = text_surface.get_rect()
        rect_text.midtop = (700, 0)
        self.screen.blit(text_surface, rect_text)
            

if __name__ == '__main__':
    ally_ship = Aliado()
    menu = MenuPrincipal(ally_ship)
    while True:
        
        menu.display_menu()
        menu.handle_input()
    ally_ship.run_game()