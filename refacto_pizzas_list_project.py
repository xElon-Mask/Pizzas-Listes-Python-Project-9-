pizzas = ["4 fromages", "Végétarienne", "Hawaï", "Calzone"]

def ajouter_pizza_utilisateur(collection):
    p = input("Pizza à ajouter: ")
    collection.append(p)

def afficher(collection):
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