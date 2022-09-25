pizzas = ("4 fromages", "Végétarienne", "Hawaï", "Calzone")
# vide = ()

def ajouter_pizza_utilisateur(collection):
    pizza_utilisateur = input("Pizza à ajouter: ")
    return collection, pizza_utilisateur

def afficher(collection):
    maj_pizzas = ajouter_pizza_utilisateur(collection)
    if len(maj_pizzas) == 0:
         print("AUCUNE PIZZA")
    else:
        print("---- LISTE DES PIZZAS (", len(maj_pizzas) + len(collection) - 1, ") ----")
        for pizza in maj_pizzas:
            print(pizza)
        print()
    # afficher la 1ere pizza
        print("Première Pizza : ", maj_pizzas[0][0])
    # afficher la dernière pizza
        print("Dernière Pizza : ", maj_pizzas[-1])





# exo 2 : protéger la fonction dans le cas où on passerait une collection vide
# afficher alors "AUCUNE PIZZA"

#afficher(pizzas)
# pizza à ajouter : l'user devra ajouter sa pizza. Il faudra alors qu'elle s'affiche à la fin de la collection
# maj_pizzas = ajouter_pizza_utilisateur(pizzas)

afficher(pizzas)


