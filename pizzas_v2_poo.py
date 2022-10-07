# nom, prix, ingrédients, végétarienne

# Ajouter une nouvelle fonctionnalité qui déclare si la pizza est végétarienne ou pas
# on ajoute un paramètre optionnel, on dira par défaut qu'elle n'est pas végé
# quand la pizza est végé il faudra l'indiquer au niveau de la fonction Afficher() : rajouter - VEGETARIENNE sur le 1er print

class Pizza():
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def Afficher(self):
        if self.vegetarienne:
            print(f"PIZZA {self.nom} : {self.prix}€ - VEGETARIENNE")
        else:
            print(f"PIZZA {self.nom} : {self.prix} €")
        print(", ".join(self.ingredients))
        print()


# rajouter plusieurs pizzas
# avec une nouvelle variable pizzas qui va être un tuple de plusieurs pizzas, 3 ou 4
# chaque pizza aura un nom différent, un prix différent, et aura des ingédients différents
# et il vous est également possible de donner un nombre différent d'ingrédients entre els différents pizzas

pizzas = [ Pizza("4 fromages", 8.50, ("Brie", "Emmental", "Comté", "Parmesan"), True),
            Pizza("Tartiflette", 15.90, ("Reblochon", "Lardons", "Crème", "Oignons", "Vin Blanc")),
            Pizza("Végétarienne", 9.50, ("Poivrons", "Tomate", "Emmental", "coeur d'artichaut"), True),
            Pizza("Royale", 13.80, ("Salami", "Champigons", "Jambon", "Tomate")),
            Pizza("Océane", 5.60, ("Saumon", "Thon", "Moules", "Beurre Persillé"))
]

# ici e est une Pizza
def tri(e):
    return e.nom



pizzas.sort(key=tri)

# Utiliser une boucle pour afficher les différentes pizzas 
# (1) afficher uniquement les pizzas végétariennes, en rajoutant du code uniquement dans la boucle for
# (2) afficher uniquement les pizzas qui ne sont pas végétariennes
# (3) afficher uniquement les pizzas qui ont de la tomate
# (4) afficher uniquement les pizzas à moins de 10€

for pizza in pizzas:
    if pizza.prix < 10:
    #if "Tomate" in pizza.ingredients:
        pizza.Afficher()






