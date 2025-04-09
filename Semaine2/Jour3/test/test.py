import pytest
from collections import Counter

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def puissance(self):
        valeurs = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10,
            "valet": 11, "dame": 12, "roi": 13, "as": 14
        }
        return valeurs[self.valeur]

def evaluer_main(cartes):
    total_puissance = sum(c.puissance() for c in cartes)
    len_main = len(cartes)
    valeurs_uniq = sorted(set(c.puissance() for c in cartes))
    couleurs = [c.couleur for c in cartes]
    compteur = Counter(c.puissance() for c in cartes)
    
    if len(cartes) == 5:
        valeurs_demon = {"10", "valet", "dame", "roi", "as"}
        noms_valeurs = set(c.valeur for c in cartes)
        couleurs_set = set(c.couleur for c in cartes)
        if noms_valeurs == valeurs_demon and len(couleurs_set) == 1:
            return 2000 + total_puissance

    if len(cartes) == 1:
        return 10 + cartes[0].puissance()  # Solo

    if 2 in compteur.values():
        return 20 + total_puissance  # Dyade

    if 3 in compteur.values():
        return 80 + total_puissance  # Triade

    if len_main >= 5 and valeurs_uniq == list(range(min(valeurs_uniq), min(valeurs_uniq)+5)):
        return 100 + total_puissance  # Marche

    if len_main >= 4 and len(set(couleurs)) == 1:
        return 125 + total_puissance  # Horde

    if 4 in compteur.values():
        return 400 + total_puissance  # Tétrade

    return total_puissance
