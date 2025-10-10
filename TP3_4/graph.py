from matplotlib import pyplot as plt
import networkx as nx

"Test graph.py"

def ajouter_noeud(graphe, nd):
    """
    permet d’ajouter un noeud à un graphe. Si le noeud existe déjà dans le
    graphe, elle ne doit pas le rajouter

    Parameters:
    -----------
    graphe : dict
        Le graphe représenté sous forme {noeud: [voisins]}.
    nd : string
    """
    if nd not in graphe:
        graphe[nd] = []

def ajouter_arete(graphe, nd, nd1):
    """
    permet d’ajouter une arête à un graphe. Si l’un des noeud n’est pas dans
    le graphe, la fonction devra retourner une erreur. Si l’arête existe déjà dans le graphe, elle ne doit pas
    l’ajouter à nouveau

    Parameters:
    -----------
    graphe : dict
        Le graphe représenté sous forme {noeud: [voisins]}.
    nd, nd1 : str
        Les noeuds de l'arête.
    
    Exceptions :
    ------------
    - Si noeud ou noeud1 n'existe pas, lève une erreur ValueError.
    - Si l'arête existe déjà, ne fait rien.
    """
    if nd not in graphe or nd1 not in graphe:
        raise ValueError(f"Un des noeuds ({nd}, {nd1}) n'existe pas dans le graphe.")

    if nd1 not in graphe[nd]:
        graphe[nd].append(nd1)
