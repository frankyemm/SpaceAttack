
# Space Attack

**Space Attack** es un videojuego en 2D desarrollado en Python utilizando la librería PyGame. En este juego, el jugador controla una nave espacial que debe derrotar a los enemigos mientras evita los disparos. El juego cuenta con un menú principal, instrucciones y sonido.

## Requisitos

- **Python 3.x**: Puedes descargarlo desde [aquí](https://www.python.org/downloads/).
- **PyGame**: Librería necesaria para ejecutar el juego. Instálala con el siguiente comando:
  ```bash
  pip install pygame
  ```

## Archivos del proyecto

- `SpaceAttack.py`: Archivo principal que inicia el juego.
- `shipp.py`: Controla la nave protagonista.
- `enemy.py`: Controla la aparición y movimiento de los enemigos.
- `ajustes.py`: Contiene configuraciones globales del juego.
- `menu.py`: Controla el menú principal del juego.
- `municion.py`: Define la lógica de los disparos del jugador y los enemigos.
- `sonidos/..`: Archivos de sonido que se reproducen en el juego.
- `fotos/..`: Imágenes utilizadas en el juego.

## Cómo ejecutar el juego

1. Asegúrate de tener instalados Python y PyGame.
2. Clona o descarga este repositorio en tu máquina local.
3. Ejecuta el archivo `SpaceAttack.py` desde la terminal o línea de comandos:
   ```bash
   python SpaceAttack.py
   ```
4. El juego comenzará mostrando el **menú principal**.

## Controles

### En el Menú Principal:
- Usa las **flechas arriba/abajo** para moverte entre las opciones.
- Presiona **Enter** para seleccionar una opción.

### En el Juego:
- **Flechas izquierda/derecha**: Mueve la nave hacia los lados.
- **Flechas arriba/abajo**: Mueve la nave hacia arriba o hacia abajo.
- **Espacio**: Dispara municiones.
  
### En el menú de instrucciones:
- **Enter**: Volver al menú principal.

## Características

- **Menú Principal**: Navega entre las opciones de "Jugar", "Instrucciones" y "Salir".
- **Fondo dinámico**: El menú principal tiene un fondo de pantalla personalizado.
- **Enemigos aleatorios**: Los enemigos aparecen en posiciones aleatorias dentro del área de juego y se mueven hacia la nave protagonista.
- **Límites de movimiento**: Las naves protagonista y enemigas no puede salir de los bordes de la pantalla.
- **Disparos del enemigo**: Los enemigos pueden disparar hacia el jugador.

## Código Principal

### Menú Principal (`menu.py`)

El menú principal se encarga de mostrar las opciones, gestionar las entradas del usuario y reproducir la música de fondo.

```python
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
```

### Nave Protagonista (`prota.py`)

La clase `Shipp` controla el movimiento de la nave aliada y asegura que no se salga de los límites de la pantalla.

```python
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
```

### Enemigos (`enemy.py`)

Los enemigos se generan en posiciones aleatorias dentro de los límites del juego y se mueven hacia abajo.

```python
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

```

## Contribuciones

Si deseas contribuir a este proyecto, eres bienvenido. Puedes crear un pull request o reportar cualquier error en el juego.

## Créditos

Este juego fue creado utilizando Python y PyGame como parte de un proyecto educativo. 

---#   S p a c e A t t a c k  
 