import sqlite3
import matplotlib.pyplot as plt
from colorama import init, Fore, Style

init(autoreset=True)

DB_NAME = "maDb.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT CHECK(role IN ('admin', 'user', 'banni')) NOT NULL,
            score INTEGER CHECK(score >= 0 AND score <= 10) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print(Fore.GREEN + "Base de données initialisée.")

def show_all():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM clients")
    clients = cursor.fetchall()
    conn.close()

    if clients:
        for client in clients:
            print(Fore.CYAN + f"ID: {client[0]}, Nom: {client[1]}")
    else:
        print(Fore.YELLOW + "Aucun client trouvé.")

def add_client():
    name = input("Entrez le nom du client : ").strip()
    if len(name) < 2:
        print(Fore.RED + "Le nom doit contenir au moins 2 lettres.")
        return

    role = input("Entrez le rôle (admin/user/banni) : ").strip().lower()
    if role not in ["admin", "user", "banni"]:
        print(Fore.RED + "Rôle invalide.")
        return

    try:
        score = int(input("Entrez le score (0-10) : ").strip())
        if not (0 <= score <= 10):
            raise ValueError
    except ValueError:
        print(Fore.RED + "Score invalide.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, role, score) VALUES (?, ?, ?)", (name, role, score))
    conn.commit()
    conn.close()
    print(Fore.GREEN + "Client ajouté avec succès.")

def delete_client():
    try:
        client_id = int(input("Entrez l'ID du client à supprimer : ").strip())
    except ValueError:
        print(Fore.RED + "ID invalide.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(Fore.GREEN + "Client supprimé.")
    else:
        print(Fore.YELLOW + "Aucun client avec cet ID.")
    conn.close()

def show_client():
    try:
        client_id = int(input("Entrez l'ID du client à afficher : ").strip())
    except ValueError:
        print(Fore.RED + "ID invalide.")
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
    client = cursor.fetchone()
    conn.close()

    if client:
        print(Fore.CYAN + f"ID: {client[0]}")
        print(Fore.CYAN + f"Nom: {client[1]}")
        print(Fore.CYAN + f"Rôle: {client[2]}")
        print(Fore.CYAN + f"Score: {client[3]}")
    else:
        print(Fore.YELLOW + "Client non trouvé.")

def show_chart():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT role, COUNT(*) FROM clients GROUP BY role")
    data = cursor.fetchall()
    conn.close()

    if not data:
        print(Fore.YELLOW + "Aucune donnée pour générer le graphique.")
        return

    roles = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=roles, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des rôles")
    plt.axis('equal')
    plt.show() 

def show_help():
    print(Fore.YELLOW + """
    Commandes disponibles :
    - init_db        : Initialise la base de données avec la table clients
    - show_all       : Affiche les noms et ID de tous les clients
    - add_client     : Ajoute un nouveau client à la base de données
    - delete_client  : Supprime un client à partir de son ID
    - show_client    : Affiche les infos d un client spécifique par ID
    - show_chart     : Affiche un camembert des rôles (admin/user/banni)
    - help           : Affiche la liste des commandes
    - exit           : Quitte le programme
    """)

def main():
    print(Fore.BLUE + "=== Terminal DB ===")
    print(Fore.YELLOW + "Tapez 'help' pour la liste des commandes.")
    while True:
        command = input(Fore.WHITE + ">>> ").strip().lower()
        if command == "init_db":
            init_db()
        elif command == "show_all":
            show_all()
        elif command == "add_client":
            add_client()
        elif command == "delete_client":
            delete_client()
        elif command == "show_client":
            show_client()
        elif command == "show_chart":
            show_chart()
        elif command == "help":
            show_help()
        elif command == "exit":
            print(Fore.BLUE + "Fermeture du programme.")
            break
        else:
            print(Fore.RED + "Commande inconnue. Tapez 'help' pour voir les commandes disponibles.")



if __name__ == "__main__":
    main()
