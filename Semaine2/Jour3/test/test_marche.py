from test import Carte, evaluer_main

def test_marche():
    cartes = [
        Carte("6", "pique"), Carte("7", "coeur"),
        Carte("8", "trèfle"), Carte("9", "pique"),
        Carte("10", "carreau")
    ]
    assert evaluer_main(cartes) == 100 + 40
