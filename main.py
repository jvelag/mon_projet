<<<<<<< HEAD
X="Juan"\nprint(f"hola {X}")
=======
from utils import display_graph_from_dict
from graph import ajouter_noeud, ajouter_arete

def main():
    
    # test Figure1
    Figure1 = {
        "A": ["B"],
        "B": [],
        "C": ["A", "B"],
        "D": ["C"],
        "E": ["D", "C"]
    }
    display_graph_from_dict(Figure1)

    g = {}

    # Ajouter des noeuds
    ajouter_noeud(g, "A")
    ajouter_noeud(g, "B")
    ajouter_noeud(g, "C")
    ajouter_noeud(g, "C")
    ajouter_noeud(g, "F")

    # Ajouter des arêtes
    # ajouter_arete(graph, noeud, noeud1)
    # de noeud a noeud 1
    ajouter_arete(g, "A", "B")
    ajouter_arete(g, "C", "B")
    ajouter_arete(g, "B", "F")
    ajouter_arete(g, "F", "C")
    ajouter_arete(g, "F", "A")
    ajouter_arete(g, "A", "C")
    ajouter_arete(g, "A", "C")
    #ajouter_arete(g, "A", "D")

    display_graph_from_dict(g)

if __name__ == "__main__":
    main()
