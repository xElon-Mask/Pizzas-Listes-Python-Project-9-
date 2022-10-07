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