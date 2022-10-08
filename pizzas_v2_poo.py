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

class PizzaPersonnalisee(Pizza):

    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    # il faut utiliser une variable de classe qui sera l'index global du numéro des variables
    dernier_numero = 0

    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
    # comme cette classe hérite d'une classe parente, je dois également appelé le constructeur de ce dernier:
    # super().__init__(self, nom, prix, ingredients, vegetarienne=False)
        super().__init__("Personnalisée " + str(self.numero), 0, [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()
    
    def demander_ingredients_utilisateur(self):
        print()
        # afficher : ingrédients pour la pizza personnalisée numéro de la pizza
        print("ingédrients pour la pizza personnalisée", str(self.numero))
        while True:
            ingredient = input("Ajouter un ingrédient (ou ENTREE pour terminer):")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculer_le_prix(self):
       self.prix = self.PRIX_DE_BASE + len(self.ingredients) * self.PRIX_PAR_INGREDIENT

# rajouter plusieurs pizzas
# avec une nouvelle variable pizzas qui va être un tuple de plusieurs pizzas, 3 ou 4
# chaque pizza aura un nom différent, un prix différent, et aura des ingédients différents
# et il vous est également possible de donner un nombre différent d'ingrédients entre els différents pizzas

pizzas = [ Pizza("4 fromages", 8.50, ("Brie", "Emmental", "Comté", "Parmesan"), True),
            Pizza("Tartiflette", 15.90, ("Reblochon", "Lardons", "Crème", "Oignons", "Vin Blanc")),
            Pizza("Végétarienne", 9.50, ("Poivrons", "Tomate", "Emmental", "coeur d'artichaut"), True),
            Pizza("Royale", 13.80, ("Salami", "Champigons", "Jambon", "Tomate")),
            Pizza("Océane", 5.60, ("Saumon", "Thon", "Moules", "Beurre Persillé")),
            PizzaPersonnalisee(),
            PizzaPersonnalisee()
]

# ici e est une Pizza
def tri(e):
    return e.nom



#pizzas.sort(key=tri)

# Utiliser une boucle pour afficher les différentes pizzas 
# (1) afficher uniquement les pizzas végétariennes, en rajoutant du code uniquement dans la boucle for
# (2) afficher uniquement les pizzas qui ne sont pas végétariennes
# (3) afficher uniquement les pizzas qui ont de la tomate
# (4) afficher uniquement les pizzas à moins de 10€

for pizza in pizzas:
    #if pizza.prix < 10:
    #if "Tomate" in pizza.ingredients:
    pizza.Afficher()


# Créer plusieurs pizzas personnalisées, et afficher le numéro de la pizza





