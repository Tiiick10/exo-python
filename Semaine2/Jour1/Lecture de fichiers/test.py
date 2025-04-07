import os

OUTPUT_PATH = os.path.expanduser("~/Desktop/exo-python/Semaine2/Jour1/Lecture de fichiers/output/")

newFile = open(OUTPUT_PATH+"note.txt", "a+")
newFile.write("Bonjour tout le monde !\n")
print("fichier créé dans le dossier output")