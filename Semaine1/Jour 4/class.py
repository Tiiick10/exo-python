# Classe de base

class Animal:
    def __init__(self, nom):
        self._nom = nom

    def faire_son(self):
        return "fais un son"

    def se_deplacer(self):
        return "se déplace"

# Sous-classe Chien

class Chien(Animal):

    def faire_son(self):
        return "Wouf ! Wouf !"

    def japper(self):
        return "Le chien jappe joyeusement !"

# Sous-classe Oiseau

class Oiseau(Animal):

    def faire_son(self):
        return "Cui Cui"

    def se_deplacer(self):
        return f"{self._nom} vole dans le ciel."

# Instances

chien1 = Chien("Rex")
oiseau1 = Oiseau("Pico")

# Méthodes chien1

print(f"Nom du chien : {chien1._nom}")
print(chien1.faire_son())
print(chien1.se_deplacer())
print(chien1.japper())

# Méthodes oiseau1

print(f"Nom de l'oiseau : {oiseau1._nom}")
print(oiseau1.faire_son())
print(oiseau1.se_deplacer())
