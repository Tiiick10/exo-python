import time

while True:
    try:
        nombre = int(input("Entrez un nombre pour le compte à rebours : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

while nombre > 0:
    print(nombre)
    time.sleep(1)
    nombre -= 1

print("Compte à rebours terminé !")
