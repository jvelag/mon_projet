import pygame

class Grid:
    """Classe représentant la grille 5x9 du manoir."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cell_size = 60  # Taille d'une cellule en pixels
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]  # Chaque case contient une salle (ou None)

    def draw(self, screen):
        """Affiche la grille à l'écran."""
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(
                    col * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                pygame.draw.rect(screen, (50, 50, 50), rect, 1)  # Grille en gris clair

    def get_cell_at(self, x, y):
        """Retourne la case de la grille aux coordonnées (x, y)."""
        return self.grid[y][x]