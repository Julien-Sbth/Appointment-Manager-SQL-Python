# patient.py

import sqlite3

class Patient:
    def __init__(self, prenom, nom, age, sex):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.sex = sex

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
                    sex TEXT NOT NULL
                )
            ''')

            # Insertion du patient dans la base de données
            cursor.execute('''
                INSERT INTO patient (prenom, nom, age, sex)
                VALUES (?, ?, ?, ?)
            ''', (self.prenom, self.nom, self.age, self.sex))

            connection.commit()
            connection.close()
            print("Le patient a été ajouté à la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout du patient : {e}")
