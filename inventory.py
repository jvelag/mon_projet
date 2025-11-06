class Inventory:
    """Classe gérant l'inventaire du joueur."""
    def __init__(self):
        self.steps = 70  # Pas initiaux
        self.gems = 2    # Gemmes initiales
        self.keys = 0    # Clés initiales
        self.dices = 0   # Dés initiaux
        self.coins = 0   # Pièces d'or initiales
        # Objets permanents (ex: pelle, marteau)
        self.permanent_items = []

    def add_item(self, item_type, quantity=1):
        """Ajoute un objet à l'inventaire."""
        if item_type == "steps":
            self.steps += quantity
        elif item_type == "gems":
            self.gems += quantity
        elif item_type == "keys":
            self.keys += quantity
        elif item_type == "dices":
            self.dices += quantity
        elif item_type == "coins":
            self.coins += quantity

    def remove_item(self, item_type, quantity=1):
        """Retire un objet de l'inventaire."""
        if item_type == "steps" and self.steps >= quantity:
            self.steps -= quantity
        elif item_type == "gems" and self.gems >= quantity:
            self.gems -= quantity
        elif item_type == "keys" and self.keys >= quantity:
            self.keys -= quantity
        elif item_type == "dices" and self.dices >= quantity:
            self.dices -= quantity