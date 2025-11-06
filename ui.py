import pygame

class UI:
    """Classe gérant l'interface utilisateur (inventaire, menus, etc.)."""
    def __init__(self, screen, inventory):
        self.screen = screen
        self.inventory = inventory
        self.font = pygame.font.SysFont("Arial", 16)

    def draw_inventory(self):
        """Affiche l'inventaire à l'écran."""
        # Position du panel d'inventaire (en bas à droite)
        x, y = 500, 500
        # Affichage des ressources
        texts = [
            f"Pas: {self.inventory.steps}",
            f"Gemmes: {self.inventory.gems}",
            f"Clés: {self.inventory.keys}",
            f"Dés: {self.inventory.dices}",
            f"Pièces: {self.inventory.coins}"
        ]
        for i, text in enumerate(texts):
            rendered_text = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(rendered_text, (x, y + i * 20))