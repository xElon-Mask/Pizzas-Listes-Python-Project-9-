pizzas = ("4 fromages", "Végétarienne", "Hawaï", "Calzone")
vide = ()

def afficher(collection):
    if len(collection) == 0:
         print("AUCUNE PIZZA")
    else:
        print("---- LISTE DES PIZZAS (", len(collection), ") ----")
        for pizza in collection:
            print(pizza)
            # exo 1
        print()
    # afficher la 1ere pizza
        print("Première Pizza : ", collection[0])
    # afficher la dernière pizza
        print("Dernière Pizza : ", collection[-1])



afficher(pizzas)

# exo 2 : protéger la fonction dans le cas où on passerait une collection vide
# afficher alors "AUCUNE PIZZA"