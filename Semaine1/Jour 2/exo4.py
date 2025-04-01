import math

billets_100 = 10
billets_50 = 10
billets_20 = 10
billets_10 = 10
billets_5 = 10

while True:
    try:
        montant = int(input("Entrez le montant à retirer : "))
        if montant <= 0:
            print("Entrez un montant positif.")
            continue

        if montant % 5 != 0:
            montant_arrondi = math.ceil(montant / 5) * 5
            print(f"Le montant a été arrondi à {montant_arrondi}€ car il doit être un multiple de 5.")
            confirmation = input("Souhaitez-vous continuer avec ce montant ? (o/n) : ").lower()
            if confirmation == "o":
                montant = montant_arrondi
                break
            else:
                print("Entrez un nouveau montant.")
        else:
            break
    except ValueError:
        print("Entrez un nombre entier.")

# Stockage des billets distribués

nb_100 = 0
nb_50 = 0
nb_20 = 0
nb_10 = 0
nb_5 = 0

while montant > 0:
    if montant >= 100 and billets_100 > 0:
        nb_100 += 1
        billets_100 -= 1
        montant -= 100
    elif montant >= 50 and billets_50 > 0:
        nb_50 += 1
        billets_50 -= 1
        montant -= 50
    elif montant >= 20 and billets_20 > 0:
        nb_20 += 1
        billets_20 -= 1
        montant -= 20
    elif montant >= 10 and billets_10 > 0:
        nb_10 += 1
        billets_10 -= 1
        montant -= 10
    elif montant >= 5 and billets_5 > 0:
        nb_5 += 1
        billets_5 -= 1
        montant -= 5
    else:
        print("Erreur : Pas assez de billets disponibles.")
        break

if montant == 0:
    print("Billets distribués :")
    if nb_100 > 0:
        print(f"{nb_100} billet(s) de 100€")
    if nb_50 > 0:
        print(f"{nb_50} billet(s) de 50€")
    if nb_20 > 0:
        print(f"{nb_20} billet(s) de 20€")
    if nb_10 > 0:
        print(f"{nb_10} billet(s) de 10€")
    if nb_5 > 0:
        print(f"{nb_5} billet(s) de 5€")
