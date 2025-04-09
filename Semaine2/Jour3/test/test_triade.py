from test import Carte, evaluer_main

def test_triade():
    cartes = [Carte("8", "pique"), Carte("8", "coeur"), Carte("8", "trèfle")]
    assert evaluer_main(cartes) == 80 + 24
