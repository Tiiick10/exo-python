somme = 0

while True:

    saisie = input("Entrez un nombre (ou 0 pour terminer) : ")

    try:

        nombre = float(saisie)

    except ValueError:
        
        print("Erreur : vous devez entrer un nombre valide.")

        continue

    if nombre == 0:

        break

    somme += nombre

print("La somme des nombres entrés est :", somme)
