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

def afficher(collection):
    collection.sort()
    if len(collection) == 0:
         print("AUCUNE PIZZA")
    else:
        print("---- LISTE DES PIZZAS (", len(collection), ") ----")
        for pizza in collection:
            print(pizza)
        print()
    # afficher la 1ere pizza
        print("Première Pizza : ", collection[0])
    # afficher la dernière pizza
        print("Dernière Pizza : ", collection[-1])

ajouter_pizza_utilisateur(pizzas)
afficher(pizzas)


