def A_Star(start_nœud, stop_nœud):

    open_set = set(start_nœud)
    closed_set = set()
    parent = {}  # parent contient une carte de contiguïté de tous les nœuds
    g = {}  # stocker la distance par rapport au nœud de départ

    # la distance du nœud de départ par rapport à lui-même est nulle
    g[start_nœud] = 0


    # start_nœud est le nœud racine, c'est-à-dire qu'il n'a pas de nœuds parent
    # donc start_nœud est défini sur son propre nœud parent
    parent[start_nœud] = start_nœud

    while len(open_set) > 0:
        n = None
        # le nœud avec le plus petit f () est trouvé
        for i in open_set:
            if n == None or g[i] + h(i) < g[n] + h(n):
                n = i
        if n == stop_nœud or Graphe[n] == None:
            pass
        else:
            for (a, b) in get_neighbor(n):
                # les nœuds a qui ne figurent pas dans le premier et le dernier ensemble sont ajoutés en premier
                # n est défini comme son parent
                if a not in open_set and a not in closed_set:
                    open_set.add(a)
                    parent[a] = n
                    g[a] = g[n] + b


                # pour chaque nœud a,compare sa distance depuis le début
                # du début au nœud n
                else:
                    if g[a] > g[n] + b:
                        # modifier g(a)
                        g[a] = g[n] + b
                        # changer le parent de a en n
                        parent[a] = n

                        # si a dans un ensemble fermé, supprimer et ajouter pour ouvrir
                        if a in closed_set:
                            closed_set.remove(a)
                            open_set.add(a)

        if n == None:
            print('chemin n''existe pas')
            return None

        # si le nœud courant est le stop_nœud
        # puis nous commençons à reconstruire le chemin de celui-ci au nœud de depart
        if n == stop_nœud:
            chemin = []

            while parent[n] != n:
                chemin.append(n)
                n = parent[n]

            chemin.append(start_nœud)

            chemin.reverse()

            print('Le chemin le plus court trouvé : {}'.format(chemin))
            return chemin

        # supprimer n de open_list, et l'ajouter à closed_list
        # parce que tous ses voisins ont été inspectés
        open_set.remove(n)
        closed_set.add(n)

    print('Le chemin nest pas trouvé')
    return None


# définir la fonction de retour du voisin et sa distance à partir du nœud passé
def get_neighbor(t):
    if t in Graphe:
        return Graphe[t]
    else:
        return None


# pour simplifier, nous considérerons les distances heuristiques données et cette fonction renvoie la distance heuristique pour tous les nœuds
def h(n):
    heur_distance = {
        'A': 10,
        'B': 5,
        'C': 5,
        'D': 10,
        'E': 10,
        'F': 3,
        'G': 3,
        'H': 3,
        'I': 0   }

    return heur_distance[n]


# Entrer les informations du graphe
Graphe = {
    'A': [('D', 5), ('C', 5)],
    'B': [('E', 5),('C', 3),('F', 3),('G', 4),('I', 5)],
    'C': [('D', 6),('H', 3),('F', 2)],
    'D': [('E', 2)],
    'F': [('G', 3)],
    'G': [('I', 3)],
    'H': [('I', 4)] }

# Exécution
A_Star('A', 'I')

