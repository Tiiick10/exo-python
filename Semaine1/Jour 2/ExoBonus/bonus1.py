while True:
    try:
        n = int(input("Entrez un nombre supérieur à 2 : "))
        if n > 2:
            break
        else:
            print("Le nombre doit être supérieur à 2.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

for i in range(2, n + 1):
    est_premier = True
    for div in range(2, int(i ** 0.5) + 1): # On teste si 49 est divisible par un nombre entre 2 et 7. 
                                            # Si 49 est divisible par 7, on sait que 49 n’est pas premier (car 7 × 7 = 49).
                                            # Si on dépasse 7 on retombe sur des diviseurs déjà testés (dans l’autre sens, genre 49 ÷ 7 = 7).
        if i % div == 0:
            est_premier = False
            break
    if est_premier:
        print(i)
