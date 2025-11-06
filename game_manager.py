import pygame
from grid import Grid
from player import Player
from inventory import Inventory
from ui import UI

class GameManager:
    """Classe principale du jeu. Gère la boucle de jeu, les événements, et l'affichage."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Prince")
        self.clock = pygame.time.Clock()
        self.running = True
        # Initialisation des modules
        self.grid = Grid(5, 9)
        self.player = Player(self.grid)
        self.inventory = Inventory()
        self.ui = UI(self.screen, self.inventory)

    def handle_events(self):
        """Gère les événements pygame (clavier, souris, etc.)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events(event.key)

    def handle_key_events(self, key):
        """Gère les touches pressées pour déplacer le joueur."""
        if key == pygame.K_z:
            self.player.move_up()
        elif key == pygame.K_s:
            self.player.move_down()
        elif key == pygame.K_q:
            self.player.move_left()
        elif key == pygame.K_d:
            self.player.move_right()

    def update(self):
        """Met à jour l'état du jeu."""
        self.player.update()

    def draw(self):
        """Affiche tous les éléments à l'écran."""
        self.screen.fill((0, 0, 0))  # Fond noir
        self.grid.draw(self.screen)
        self.player.draw(self.screen)
        self.ui.draw_inventory()

    def run(self):
        """Boucle principale du jeu."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()