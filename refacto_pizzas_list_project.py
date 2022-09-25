pizzas = ["4 fromages", "Végétarienne", "Hawaï", "Calzone"]
vide = ()

def pizza_existe(collection, e):
    for i in collection:
        if i == e:
            return True
    return False

def ajouter_pizza_utilisateur(collection):
    p = input("Pizza à ajouter: ")
    # verif = pizza_existe(collection, p)
    if p.lower() in collection:
        print("ERREUR : Cette pizza est déjà disponible dans la liste")
    else:
        collection.append(p)

def afficher(collection, n_premiers_elements=-1):
    #collection.sort()
    c = collection
    if not n_premiers_elements == -1:
        c = collection[:n_premiers_elements]
    if len(c) == 0:
         print("AUCUNE PIZZA")
    else:
        print("---- LISTE DES PIZZAS (", len(c), ") ----")
        for pizza in c:
            print(pizza)
        print()
    # afficher la 1ere pizza
        print("Première Pizza : ", c[0])
    # afficher la dernière pizza
        print("Dernière Pizza : ", c[-1])

ajouter_pizza_utilisateur(pizzas)
afficher(vide, 3)


# afficher uniquement les 2 ou 3 premières pizzas.
# modifier la fonction afficher pour passer un paramètre : si afficher(pizzas, 3) il n'affichera que les 3 premières pizzas
# attention, c'est un paramètre optionnel, si on ne passe aucun chiffre cela doit continuer à fonctionner comme avant (afficher toutes les pizzas)
