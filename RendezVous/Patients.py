# patient.py

import sqlite3

class Patient:
    def __init__(self, prenom, nom, age, sexe):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.sexe = sexe

    def add_to_database(self):
        try:
            connection = sqlite3.connect('database.sqlite')  # Chemin relatif pour la base de données
            cursor = connection.cursor()

            # Création de la table si elle n'existe pas déjà
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS patient (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prenom TEXT NOT NULL,
                    nom TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    sexe TEXT NOT NULL
                )
            ''')

            # Insertion du patient dans la base de données
            cursor.execute('''
                INSERT INTO patient (prenom, nom, age, sexe)
                VALUES (?, ?, ?, ?)
            ''', (self.prenom, self.nom, self.age, self.sexe))

            connection.commit()
            connection.close()
            print("Le patient a été ajouté à la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout du patient : {e}")

    def remove_from_database(self):
<<<<<<< HEAD
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                DELETE FROM patient
                WHERE prenom = ?
            ''', (self.prenom,))

            connection.commit()
            connection.close()
            print("Le patient a été supprimé de la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression du patient : {e}")
=======
            try:
                connection = sqlite3.connect('database.sqlite')
                cursor = connection.cursor()

                cursor.execute('''
                    DELETE FROM patient
                    WHERE prenom = ? AND nom = ? AND age = ? AND sexe = ?
                ''', (self.prenom, self.nom, self.age, self.sexe))

                connection.commit()
                connection.close()
                print("Le patient a été supprimé de la base de données avec succès.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la suppression du patient : {e}")
>>>>>>> bdcac5c3b115d04c74bffff4ef682db9600d8970

    @staticmethod
    def Modif_Patient(prenom, nom, age, sex):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
<<<<<<< HEAD
                                UPDATE patient
                                SET nom = ?, age = ?, sex = ?
                                WHERE prenom = ?
                            ''', (nom, age, sex, prenom))
=======
                                    UPDATE patient
                                    SET nom = ?, age = ?, sex = ?
                                    WHERE prenom = ?
                                ''', (nom, age, sex, prenom))
>>>>>>> bdcac5c3b115d04c74bffff4ef682db9600d8970

            connection.commit()
            connection.close()
            print("Les informations du patient ont été mises à jour avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la mise à jour des informations du patient : {e}")
<<<<<<< HEAD
=======

>>>>>>> bdcac5c3b115d04c74bffff4ef682db9600d8970
    @staticmethod
    def AllDisplayDataFromPatient():
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
<<<<<<< HEAD
                    SELECT PatientID, prenom, nom FROM patient
                ''')
=======
                SELECT SecretaireID,Nom,Prenom FROM patient
            ''')
>>>>>>> bdcac5c3b115d04c74bffff4ef682db9600d8970

            rows = cursor.fetchall()
            connection.close()

            if rows:
<<<<<<< HEAD
                formatted_data = [list(row) for row in rows]  # Convertit chaque tuple en liste
                for data in formatted_data:
                    print(data)  # Affiche chaque liste de données
                return formatted_data  # Retourne les données formatées
            else:
                print("La table 'patient' est vide.")
                return []  # Retourne une liste vide si aucune donnée trouvée
        except sqlite3.Error as e:
            print(f"Erreur lors de l'affichage des patients : {e}")




=======
                print("Liste des secretaires :")
                for row in rows:
                    print(list(row))
                return rows
            else:
                print("La table 'secretaire' est vide.")
                return []
        except sqlite3.Error as e:
            print(f"Erreur lors de l'affichage des secretaires : {e}")
>>>>>>> bdcac5c3b115d04c74bffff4ef682db9600d8970
