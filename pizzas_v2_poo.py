# nom, prix, ingrédients, végétarienne

class Pizza():
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def Afficher(self):
        print(f"PIZZA {self.nom} : {self.prix} €")

pizza1 = Pizza("4 fromages", 8.50)
pizza1.Afficher()