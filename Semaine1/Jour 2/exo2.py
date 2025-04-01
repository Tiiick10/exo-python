somme = 0

while True:
    nombre = float(input("Entrez un nombre (ou 0 pour terminer) : "))

    if nombre == 0:
        break

    somme += nombre

print("La somme des nombres entrés est :", somme)
