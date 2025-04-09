import requests, bs4, os, random
import tempfile
from PyPDF2 import PdfReader, PdfWriter
import img2pdf
import re

OUTPUT_PATH = os.path.expanduser('~/Desktop/exo-python/Semaine2/Jour2/output/')#C:/Users/Win/OneDrive/Bureau/exo-python/Semaine2/Jour2/output/
OUTPUT_DL_PATH = os.path.expanduser('~/Desktop/exo-python/Semaine2/Jour2/output/download/')#C:/Users/Win/OneDrive/Bureau/exo-python/Semaine2/Jour2/output/download/
os.makedirs(OUTPUT_DL_PATH, exist_ok=True)
WEBSITE_PATH = "https://www.creativeuncut.com/"
IMAGE_HOST_PREFIX = "https://sjc1.vultrobjects.com/cucdn/"

def showHelp():
    print("""
Commandes disponibles :
───────────────────────
get_title          → Affiche le titre d'une galerie test
get_url            → Affiche l'URL de la première image d'une galerie
get_img            → Affiche l'URL de l'image d'une page donnée
get_next           → Affiche l'URL de l'image suivante
download           → Télécharge une image depuis une URL directe
download_all       → Télécharge toutes les images d'une galerie
random_gallery     → Propose une galerie aléatoire et permet de la télécharger
list_galleries     → Affiche la liste de toutes les galeries disponibles
search_gallery     → Recherche une galerie par mot-clé et permet d'en télécharger plusieurs
make_pdf           → Crée un PDF à partir des images d'une galerie déjà téléchargée
clear_images       → Supprime les images d'une galerie téléchargée
help               → Affiche cette aide
exit               → Quitte le programme
""")

def getGalleryTitle():
    url = "https://www.creativeuncut.com/art_mario-kart-world_a.html"
    try:
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        title = soup.find("h1").text.strip()
        print(title)

    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

def getFirstUrl(galleryUrl):
    
    try:
        response = requests.get(galleryUrl)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        gallery = soup.find("div", class_="glry")
        
        if not gallery:
            print("Galerie introuvable.")
            return None
        
        first_img = gallery.find("a")
        
        if first_img and "href" in first_img.attrs:
            img_url = first_img["href"]
            
            print(f"URL de l'image : https://www.creativeuncut.com/{img_url.lstrip('/')}")
        
        else:
            print("Aucune image trouvée")
            return None

    except Exception as e:
        print(f"Error fetching URL : {e}")
        return None

def getNextUrl(actualUrl:str, galleryName="")->int|None:
    nextUrl = "https://www.creativeuncut.com/gallery-48/mkw-logo.html"
    try:
        response = requests.get(actualUrl)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        imgName = soup.select("#g_nav_r a")[0]["href"]

        if galleryName == "":
            galleryName = actualUrl.split("/")[3]
        return WEBSITE_PATH+galleryName+"/"+imgName

    except Exception as e:
        print(f"Error fetching URL: {e}")
        return

def getImgUrl(pageUrl:str, galleryName="")->str|None:
    try:
        if galleryName == "":
            galleryName = pageUrl.split("/")[3]
        response = requests.get(pageUrl)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        imgName = soup.select("#g_image img")[0]["src"]
        return IMAGE_HOST_PREFIX+galleryName+"/"+imgName

    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

def downloadImg(url, imgName="", output_path=OUTPUT_PATH)->bool:
    if imgName == "":
        imgName = url.split("/")[-1]
    try:
        output_file_path = os.path.join(output_path, imgName)
        response = requests.get(url).content
        with open(output_file_path, 'wb') as handler:
            handler.write(response)
            handler.close()
            return True
    except Exception as e:
        print(f"Error downloading image: {e}")
        return False

def downloadAllImgByGalleryUrl(gallery_url):
    try:
        response = requests.get(gallery_url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        gallery = soup.find("div", class_="glry")

        if not gallery:
            print("Gallery not found")
            return

        title = soup.find("h1").text.strip()
        safe_title = re.sub(r'\W+', '_', title)

        download_path = os.path.join(OUTPUT_DL_PATH, safe_title)
        os.makedirs(download_path, exist_ok=True)

        first_img_link = gallery.find("a")
        if not first_img_link or "href" not in first_img_link.attrs:
            print("First image not found")
            return

        first_img_page = WEBSITE_PATH + first_img_link["href"].lstrip("/")
        gallery_name = first_img_page.split("/")[3]

        current_page = first_img_page
        count = 1

        while current_page:
            img_url = getImgUrl(current_page, gallery_name)
            if img_url:
                print(f"DL Image {count}: {img_url}")
                downloadImg(img_url, output_path=download_path)
                count += 1
            else:
                print("Image not found")
                break

            next_url = getNextUrl(current_page, gallery_name)
            if not next_url or next_url == current_page:
                break
            current_page = next_url

        print("Download done")
        convert_img_to_pdf(title)

    except Exception as e:
        print(f"Error while downloading : {e}")

def getAllGameName():

    url = "https://www.creativeuncut.com/game-art-galleries.html"
    result = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all("div", class_="ag")

        for div in divs:
            a_tag = div.find("a")
            if a_tag and "href" in a_tag.attrs:
                name = a_tag.text.strip()
                if name.endswith("The"):
                    name = "The " + name[:-4].strip()
                href = WEBSITE_PATH + a_tag["href"].lstrip("/")
                result.append({"name": name, "url": href})

        return result

    except Exception as e:
        print(f"Erreur lors de la récupération des galeries : {e}")
        return []

def getRandomGallery():
    all_games = getAllGameName()
    if not all_games:
        print("Aucune galerie trouvée.")
        return

    random_game = random.choice(all_games)
    print(f"Galerie aléatoire : {random_game['name']}")
    print(f"URL : {random_game['url']}")

    user_input = input("Souhaitez-vous télécharger cette galerie ? (o/n) : ").lower()
    if user_input == 'o':
        downloadAllImgByGalleryUrl(random_game['url'])
    else:
        print("Annulé.")

def searchGallery():
    search_term = input("Entrez un mot-clé pour rechercher une galerie (attention à la casse ex: pokémon et non pokemon) : ").lower()
    galleries = getAllGameName()
    filtered = [g for g in galleries if search_term in g["name"].lower()]

    if not filtered:
        print("Aucune galerie trouvée.")
        return

    for i, g in enumerate(filtered, 1):
        print(f"{i}. {g['name']} -> {g['url']}")

    choix = input("Quels galeries veux-tu DL? (ex: 1 2 3 ou all pour tout / vide pour annuler) : ").lower()
    if not choix.strip():
        print("Aucun téléchargement effectué.")
        return

    try:
        if choix == "all":
            selected = range(1, len(filtered)+1)
        else:
            selected = [int(x) for x in choix.strip().split()]

        for i in selected:
            if 1 <= i <= len(filtered):
                print(f"Téléchargement de : {filtered[i-1]['name']}")
                downloadAllImgByGalleryUrl(filtered[i-1]["url"])
            else:
                print(f"Numéro {i} invalide.")
    except ValueError:
        print("Entrée invalide.")

def convert_img_to_pdf(gallery_title: str):

    safe_title = re.sub(r'\W+', '_', gallery_title)
    gallery_folder = os.path.join(OUTPUT_DL_PATH, safe_title)

    if not os.path.exists(gallery_folder):
        print(f"Le dossier '{gallery_folder}' n'existe pas.")
        return

    images = [f for f in os.listdir(gallery_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()

    if not images:
        print("Aucune image trouvée pour créer un PDF.")
        return

    image_paths = [os.path.join(gallery_folder, img) for img in images]
    output_pdf_path = os.path.join(gallery_folder, f"{safe_title}.pdf")

    try:
        with open(output_pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_paths))
        print(f"PDF créé : {output_pdf_path}")
    except Exception as e:
        print(f"Erreur lors de la création du PDF : {e}")

def clear_images_in_folder():
    title = input("Titre de la galerie à nettoyer (ex: Mario Kart World) : ")
    safe_title = re.sub(r'\W+', '_', title)
    gallery_folder = os.path.join(OUTPUT_DL_PATH, safe_title)

    if not os.path.exists(gallery_folder):
        print(f"Le dossier '{gallery_folder}' n'existe pas.")
        return

    images_deleted = 0
    for file in os.listdir(gallery_folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            try:
                os.remove(os.path.join(gallery_folder, file))
                images_deleted += 1
            except Exception as e:
                print(f"Erreur en supprimant {file} : {e}")

    if images_deleted == 0:
        print("Aucune image à supprimer.")
    else:
        print(f"{images_deleted} image(s) supprimée(s) de '{safe_title}'")

print("----- PDF ART -----")
showHelp()

while True:
    cmd = input(">>>")

    if cmd == "exit":
        print("Bye")
        break

    if cmd == "get_title":
        getGalleryTitle()

    if cmd == "get_url":
        url = input("Entrez l'URL de la galerie : ")
        getFirstUrl(url)

    if cmd == "get_img":
        url = input("Entrez l'URL de la galerie : ") #https://www.creativeuncut.com/gallery-48/mkw-logo.html
        print(getImgUrl(url))
    
    if cmd == "get_next":
        url = input("Entrez l'URL de la galerie : ") #https://www.creativeuncut.com/gallery-48/mkw-logo.html
        print(getNextUrl(url))

    if cmd == "download":
        url = input("Entrez l'URL de la galerie : ") #https://sjc1.vultrobjects.com/cucdn/gallery-48/art/mkw-logo.jpg
        print(downloadImg(url))

    if cmd == "download_all":
        url = input("Entrez l'URL de la galerie : ") #https://www.creativeuncut.com/art_mario-kart-world_a.html
        downloadAllImgByGalleryUrl(url)
    
    if cmd == "random_gallery":
        getRandomGallery()

    if cmd == "list_galleries":
        galleries = getAllGameName()
        if not galleries:
            print("Aucune galerie trouvée.")
        else:
            for i, game in enumerate(galleries, 1):
                print(f"{i}. {game['name']} -> {game['url']}")

    if cmd == "search_gallery":
        searchGallery()
    
    if cmd == "make_pdf":
        title = input("Entrez le titre de la galerie téléchargée : ")
        convert_img_to_pdf(title)

    if cmd == "clear_images":
        clear_images_in_folder()

    if cmd == "help":
        showHelp()






