from test import Carte, evaluer_main

def test_solo():
    cartes = [Carte("roi", "coeur")]
    assert evaluer_main(cartes) == 10 + 13