# nom, prix, ingrédients, végétarienne

class Pizza():
    def __init__(self, nom, prix, ingredients):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients

    def Afficher(self):
        print(f"PIZZA {self.nom} : {self.prix} €")
        print(", ".join(self.ingredients))

pizza1 = Pizza("4 fromages", 8.50, ("Brie", "Emmental", "Comté", "Parmesan"))
pizza1.Afficher()

# rajouter plusieurs pizzas
# avec une nouvelle variable pizzas qui va être un tuple de plusieurs pizzas, 3 ou 4
# chaque pizza aura un nom différent, un prix différent, et aura des ingédients différents
# et il vous est également possible de donner un nombre différent d'ingrédients entre els différents pizzas

pizzas = (Pizza("Tartiflette", 15.90, ("Reblochon", "Lardons", "Crème", "Oignons", "Vin Blanc")),
 Pizza("Végétarienne", 11.50, ("Poivrons", "Tomates cerises", "Emmental", "coeur d'artichaut")),
 Pizza("Royale", 13.80, ("Salami", "Champigons", "Jambon")),
 Pizza("Océane", 17.60, ("Saumon", "Thon", "Moules", "Beurre Persillé"))
)


# Utiliser une boucle pour afficher les différentes pizzas 

for pizza in pizzas:
    pizza.Afficher()