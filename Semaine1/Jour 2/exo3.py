import time

while True:

    saisie = input("Entrez un nombre pour le compte à rebours : ")
    
    try:

        nombre = int(saisie)

        if nombre <= 0:

            print("Veuillez entrer un nombre entier.")

        else:

            break

    except ValueError:

        print("Veuillez entrer un nombre entier valide.")

while nombre > 0:

    print(nombre)

    time.sleep(1)
    
    nombre -= 1

print("Compte à rebours terminé !")
