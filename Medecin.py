import sqlite3
from enum import Enum, auto


class Spe(Enum):
    PEDIATRE:auto()
    GENERALISTE:auto()
    DENTISTE:auto()

class Medecin:
    def __init__(self,specialite:Spe="",nom="",prenom="",id=0):
        self.id = id
        self.spe = specialite
        self.nom = nom
        self.prenom = prenom

    def add_to_database(self):
        try:
            connection = sqlite3.connect('database.sqlite')  # Chemin relatif pour la base de données
            cursor = connection.cursor()

            # Création de la table si elle n'existe pas déjà
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS medecin (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL,
                    specialite TEXT NOT NULL
                )
            ''')

            # Insertion du patient dans la base de données
            cursor.execute('''
                INSERT INTO medecin (nom, prenom, specialite)
                VALUES (?, ?, ?)
            ''', (self.nom, self.prenom, self.spe))

            connection.commit()
            connection.close()
            print("Le medecin a été ajouté à la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout du medecin : {e}")

    def update_from_database(self):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                   UPDATE medecin
                   SET nom = ?, prenom = ?, specialite = ?
                   WHERE id = ?
               ''', (self.nom, self.prenom, self.spe, self.id))

            connection.commit()
            connection.close()
            print("Le medecin a été modifié dans la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la modification du medecin : {e}")

    def remove_from_database(self):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                DELETE FROM medecin
                WHERE id = ?
            ''', (self.id,))

            connection.commit()
            connection.close()
            print("Le medecin a été supprimé de la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression du medecin : {e}")