import os
import subprocess


# Dossier output s’il n’existe pas

OUTPUT_PATH = os.path.expanduser("~/Desktop/exo-python/Semaine2/Jour1/filereader-projet/output/")

os.makedirs(OUTPUT_PATH, exist_ok=True)

# Dossier output pour les vidéos s’il n’existe pas

OUTPUT_VIDEO_PATH = os.path.expanduser("~/Desktop/exo-python/Semaine2/Jour1/filereader-projet/output_video/")

os.makedirs(OUTPUT_VIDEO_PATH, exist_ok=True)

def get_filename(name):
    if not name.endswith(".txt"):
        name += ".txt"
    return name

def show_help():
    print("\nCommandes disponibles :")
    print("---------------------------------")
    print("- help : Affiche l'aide")
    print("- read <nom_fichier> : Lit le contenu d'un fichier")
    print("- write <nom_fichier> : Écrit à la fin d un fichier")
    print("- create <nom_fichier> : Crée un nouveau fichier")
    print("- del <nom_fichier> : Supprime un fichier")
    print("- download <nom_fichier> : Télécharge un fichier")
    print("- exit : Quitte le terminal\n")

def read_file(args):
    if not args:
        print("Indiquer un nom de fichier.")
        print("Fichiers disponibles :", os.listdir(OUTPUT_PATH))
        return
    filename = get_filename(args[0])
    filepath = os.path.join(OUTPUT_PATH, filename)
    if not os.path.exists(filepath):
        print("Fichier introuvable.")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"\nContenu de {filename}:\n{'-'*30}\n{content}\n{'-'*30}")

def write_file(args):
    if not args:
        print("Iindiquer un nom de fichier.")
        print("Fichiers disponibles :", os.listdir(OUTPUT_PATH))
        return
    filename = get_filename(args[0])
    filepath = os.path.join(OUTPUT_PATH, filename)
    if not os.path.exists(filepath):
        print("Fichier introuvable.")
        return
    text = input("Texte à ajouter : ")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    print("Texte ajouté.")

def create_file(args):
    filename = args[0] if args else input("Entrez le nom du fichier : ")
    filename = get_filename(filename)
    filepath = os.path.join(OUTPUT_PATH, filename)
    if os.path.exists(filepath):
        print("Le fichier existe déjà.")
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("")
    print(f"Fichier {filename} créé.")

def delete_file(args):
    if not args:
        print("Veuillez indiquer le nom du fichier à supprimer.")
        return
    filename = get_filename(args[0])
    filepath = os.path.join(OUTPUT_PATH, filename)
    if not os.path.exists(filepath):
        print("Ce fichier n'existe pas.")
        return
    os.remove(filepath)
    print(f"Fichier {filename} supprimé.")

def download_video(args):
    if not args:
        print("Veuillez fournir le nom d'un fichier contenant les URLs YouTube.")
        return
    filename = get_filename(args[0])
    filepath = os.path.join(OUTPUT_PATH, filename)
    if not os.path.exists(filepath):
        print(f"Le fichier {filename} n'existe pas.")
        return
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            urls = file.readlines()
        
        if not urls:
            print(f"Le fichier {filename} est vide.")
            return

        print("Téléchargement des vidéos en cours...")
        for url in urls:
            url = url.strip()
            if not url:
                continue
            try:
                print(f"Téléchargement de : {url}")
                output_path = os.path.join(OUTPUT_VIDEO_PATH, "%(title)s.%(ext)s")
                subprocess.run(["yt-dlp", "-o", output_path, url], check=True)
                print(f"Vidéo téléchargée avec succès : {url}")
            except subprocess.CalledProcessError as e:
                print(f"Erreur lors du téléchargement de l'URL {url} : {e}")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {filename} : {e}")

# Boucle principale

print("Welcome lads ! Tapez 'help' pour la liste des commandes.")
while True:
    user_input = input(">>> ").strip().split()
    if not user_input:
        continue

    command = user_input[0].lower()
    args = user_input[1:]

    if command == "help":
        show_help()
    elif command == "read":
        read_file(args)
    elif command == "write":
        write_file(args)
    elif command == "create":
        create_file(args)
    elif command == "del":
        delete_file(args)
    elif command == "download":
        download_video(args)
    elif command == "exit":
        print("Au revoir !")
        break
    else:
        print("Commande inconnue. Tapez 'help' pour voir les commandes disponibles.")
