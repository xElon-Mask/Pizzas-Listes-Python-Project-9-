pizzas = ("4 fromages", "Végétarienne", "Hawaï", "Calzone")

def afficher(collection):
    print("---- LISTE DES PIZZAS (", len(collection), ") ----")
    for pizza in collection:
        print(pizza)


afficher(pizzas)