# nom, prix, ingrédients, végétarienne

class Pizza():
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def Afficher(self):
        print(f"PIZZA {self.nom} : {self.prix} €")

