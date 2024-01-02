import sqlite3
from enum import Enum, auto




class Medecin:
    def __init__(self, prenom="", nom="", specialite="", id=0):
        self.id = id
        self.specialite = specialite
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
            ''', (self.nom, self.prenom, self.specialite))

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
                   WHERE MedecinID = ?
               ''', (self.nom, self.prenom, self.specialite, self.id))

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
                DELETE FROM Medecin
                WHERE MedecinID = ?
            ''', (self.id,))

            connection.commit()
            connection.close()
            print("Le medecin a été supprimé de la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression du medecin : {e}")

    @staticmethod
    def displayAllData():
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                         SELECT  MedecinId,prenom, nom FROM Medecin
                     ''')

            rows = cursor.fetchall()
            connection.close()

            if rows:
                print("Liste des medecins :")
                for row in rows:
                    print(list(row))
                return rows
            else:
                print("La table 'Medecin' est vide.")
                return []
        except sqlite3.Error as e:
            print(f"Erreur lors de l'affichage des patients : {e}")
