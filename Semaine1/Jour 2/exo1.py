import random

def deviner_nombre():
    nombre_a_deviner = random.randint(1, 100)
    while True:
        try:
            proposition = int(input("Devinez le nombre (ou entrez -1 pour arrêter) : "))
            if proposition == nombre_a_deviner:
                print("Félicitations ! Vous avez deviné le bon nombre.")
                break
            elif proposition == -1:
                print("Dommage. Le nombre à deviner était :", nombre_a_deviner)
                break
            elif abs(proposition - nombre_a_deviner) < 10:
                print("Vous êtes proche !")
            elif proposition < nombre_a_deviner:
                print("Le nombre à deviner est plus grand.")
            else:
                print("Le nombre à deviner est plus petit.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

deviner_nombre()
