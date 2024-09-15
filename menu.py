import pygame
import sys

class MenuPrincipal:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.ajustes = game.ajustes
        self.font = pygame.font.SysFont("Minecraftia-Regular", 40)
        self.options = ["Jugar", "Instrucciones", "Salir"]
        self.selected_option = 0
        

    def display_menu(self):
        pygame.mixer.music.load('sonidos/menu_sound.mp3')
        pygame.mixer.music.play(-1)
        # Limpiar la pantalla
        self.screen.blit(self.ajustes.menu_background,(0,0))
        
        # Título
        title_font = pygame.font.SysFont("Minecraftia-Regular", 60)
        title_surface = title_font.render("Space Attack", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.ajustes.width // 2, 100))
        self.screen.blit(title_surface, title_rect)
        
        # Mostrar las opciones
        for i, option in enumerate(self.options):
            if i == self.selected_option:
                label = self.font.render(f"> {option} <", True, (255, 255, 0))  # Resaltar la opción seleccionada
            else:
                label = self.font.render(option, True, (255, 255, 255))
            label_rect = label.get_rect(center=(self.ajustes.width // 2, 200 + i * 60))
            self.screen.blit(label, label_rect)
        
        # Actualizar pantalla
        pygame.display.flip()

    def handle_input(self):
        # Capturar eventos del teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()

    def select_option(self):
        if self.selected_option == 0:
            self.game.run_game()  # Empieza el juego
        elif self.selected_option == 1:
            self.show_instructions()  # Mostrar las instrucciones
        elif self.selected_option == 2:
            pygame.quit()
            sys.exit()  # Salir del juego

    def show_instructions(self):
        # Mostrar pantalla de instrucciones
        self.screen.fill((0, 0, 0))
        instructions = [
            "Usa las flechas para moverte.",
            "Presiona ESPACIO para disparar.",
            "Evita los enemigos y sus disparos.",
            "Presiona ENTER para volver al menú."
        ]
        for i, line in enumerate(instructions):
            instruction_label = self.font.render(line, True, (255, 255, 255))
            label_rect = instruction_label.get_rect(center=(self.ajustes.width // 2, 150 + i * 60))
            self.screen.blit(instruction_label, label_rect)
        
        pygame.display.flip()

        # Esperar a que el usuario presione ENTER para regresar al menú
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return  # Volver al menú principal

