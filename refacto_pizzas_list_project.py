pizzas = ["4 fromages", "Végétarienne", "Hawaï", "Calzone"]

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

def afficher(collection, nb_pizzas=-1):
    collection.sort()
    if len(collection) == 0:
         print("AUCUNE PIZZA")
    else:
        print("---- LISTE DES PIZZAS (", len(collection), ") ----")
        for pizza in collection[0:nb_pizzas]:
            print(pizza)
        print(collection[-1])
        print()
    # afficher la 1ere pizza
        print("Première Pizza : ", collection[0])
    # afficher la dernière pizza
        print("Dernière Pizza : ", collection[-1])

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas, 2)


# afficher uniquement les 2 ou 3 premières pizzas.
# modifier la fonction afficher pour passer un paramètre : si afficher(pizzas, 3) il n'affichera que les 3 premières pizzas
# attention, c'est un paramètre optionnel, si on ne passe aucun chiffre cela doit continuer à fonctionner comme avant (afficher toutes les pizzas)
