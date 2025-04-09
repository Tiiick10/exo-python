from test import Carte, evaluer_main

def test_tetrade():
    cartes = [
        Carte("4", "pique"), Carte("4", "coeur"),
        Carte("4", "trèfle"), Carte("4", "carreau"),
        Carte("7", "pique")
    ]
    assert evaluer_main(cartes) == 400 + (4*4 + 7)

def test_tetrade_pas_valide_si_que_3():
    cartes = [
        Carte("9", "coeur"), Carte("9", "pique"),
        Carte("9", "trèfle"), Carte("2", "carreau"),
        Carte("3", "carreau")
    ]
    assert evaluer_main(cartes) == 80 + (9*3 + 2 + 3)


