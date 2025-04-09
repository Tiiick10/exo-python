from test import Carte, evaluer_main

def test_aucune_combinaison():
    cartes = [Carte("3", "pique"), Carte("7", "coeur"), Carte("9", "trèfle")]
    assert evaluer_main(cartes) == 19
