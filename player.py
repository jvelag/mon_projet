import pygame

class Player:
    """Classe représentant le joueur et sa position dans la grille."""
    def __init__(self, grid):
        self.grid = grid
        self.x = 0  # Position initiale (colonne)
        self.y = 0  # Position initiale (ligne)
        self.color = (0, 255, 0)  # Couleur du curseur (vert)

    def move_up(self):
        """Déplace le joueur vers le haut."""
        if self.y > 0:
            self.y -= 1

    def move_down(self):
        """Déplace le joueur vers le bas."""
        if self.y < self.grid.rows - 1:
            self.y += 1

    def move_left(self):
        """Déplace le joueur vers la gauche."""
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        """Déplace le joueur vers la droite."""
        if self.x < self.grid.cols - 1:
            self.x += 1

    def update(self):
        """Met à jour la position du joueur (si nécessaire)."""
        pass  # À compléter plus tard

    def draw(self, screen):
        """Affiche le curseur du joueur."""
        cell_size = self.grid.cell_size
        rect = pygame.Rect(
            self.x * cell_size,
            self.y * cell_size,
            cell_size,
            cell_size
        )
        pygame.draw.rect(screen, self.color, rect, 2)  # Dessine un rectangle vert