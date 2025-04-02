nombre_ligne = ""

while True:
    try:
        nombre_ligne = int(input('entrez un nombre postif'))
    except ValueError:
        print('valeur incorrecte !')
        continue
    if nombre_ligne > 0:
        print('entrez un nombre plus grand que 2')
        continue
    break

for i in range(1, nombre_ligne+1):
    espace = nombre_ligne-i
    for j in range(espace):
        print(f"  ",end="")
    for j in range(i, 2*i):
        print(j,end=" ")
    for j in range(2*i-2, i-1, -1):
        print(j,end=" ")
    print()