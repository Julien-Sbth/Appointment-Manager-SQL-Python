import sqlite3


class Secretaire:

    def __init__(self, Prenom, nom, id=0):
        self.Prenom = Prenom
        self.nom = nom
        self.id = id

    def add_to_database(self):
        try:
            connection = sqlite3.connect('database.sqlite')  # Chemin relatif pour la base de données
            cursor = connection.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS secretaire (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom TEXT NOT NULL,
                    prenom TEXT NOT NULL
                )
            ''')

            cursor.execute('''
                INSERT INTO secretaire (nom, prenom)
                VALUES (?, ?)
            ''', (self.nom, self.Prenom))

            connection.commit()
            connection.close()
            print("Le secretaire a été ajouté à la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout du secretaire : {e}")

    def update_from_database(self):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                   UPDATE secretaire
                   SET nom = ?, prenom = ?
                   WHERE SecretaireId = ?
               ''', (self.nom, self.Prenom, self.id))

            connection.commit()
            connection.close()
            print("Le secretaire a été modifié dans la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la modification du secretaire : {e}")

    def remove_from_database(self):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                DELETE FROM secretaire
                WHERE SecretaireId = ?
            ''', (self.id,))

            connection.commit()
            connection.close()
            print("Le secretaire a été supprimé de la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression du secretaire : {e}")

    @staticmethod
    def displayAllData():
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                       SELECT SecretaireId, prenom, nom FROM Secretaire
                   ''')

            rows = cursor.fetchall()
            connection.close()

            if rows:
                print("Liste des patients :")
                for row in rows:
                    print(list(row))
                return rows
            else:
                print("La table 'patient' est vide.")
                return []
        except sqlite3.Error as e:
            print(f"Erreur lors de l'affichage des patients : {e}")
