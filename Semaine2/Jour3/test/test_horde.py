from test import Carte, evaluer_main

def test_horde():
    cartes = [
        Carte("2", "coeur"), Carte("5", "coeur"),
        Carte("7", "coeur"), Carte("9", "coeur")
    ]
    assert evaluer_main(cartes) == 125 + 23
