from test import Carte, evaluer_main

def test_dyade():
    cartes = [Carte("5", "pique"), Carte("5", "coeur")]
    assert evaluer_main(cartes) == 20 + 10
