from test import Carte, evaluer_main

def test_main_demon():
    cartes = [
        Carte("10", "coeur"), Carte("valet", "coeur"),
        Carte("dame", "coeur"), Carte("roi", "coeur"),
        Carte("as", "coeur")
    ]
    assert evaluer_main(cartes) == 2000 + 60

def test_main_demon_invalide_valeur():
    cartes = [
        Carte("9", "coeur"), Carte("valet", "coeur"),
        Carte("dame", "coeur"), Carte("roi", "coeur"),
        Carte("as", "coeur")
    ]
    assert evaluer_main(cartes) != 2000 + 57

def test_main_demon_invalide_couleur():
    cartes = [
        Carte("10", "coeur"), Carte("valet", "coeur"),
        Carte("dame", "pique"), Carte("roi", "coeur"),
        Carte("as", "coeur")
    ]
    assert evaluer_main(cartes) != 2000 + 60
