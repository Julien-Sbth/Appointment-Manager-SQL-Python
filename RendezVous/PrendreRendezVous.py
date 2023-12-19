import sqlite3


class RendezVous:

    def __init__(self, date, heure, patient, medecin, secretaire):
        self.date = date
        self.heure = heure
        self.patient = patient
        self.medecin = medecin
        self.secretaire = secretaire

    @staticmethod
    def prendre_rendezvous(date, heure, medecin, secretaire, patient):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS RendezVous (
                        RendezVousID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Date INTEGER NOT NULL,
                        Heure TEXT NOT NULL,
                        IDMedecin INTEGER NOT NULL,
                        IDSecretaire INTEGER NOT NULL,
                        IDPatient INTEGER NOT NULL,
                        FOREIGN KEY (IDMedecin) REFERENCES Medecin(MedecinID),
                        FOREIGN KEY (IDSecretaire) REFERENCES Secretaire(SecretaireID),
                        FOREIGN KEY (IDPatient) REFERENCES Patient(PatientID)
                    )
                ''')

            cursor.execute('''
                    INSERT INTO RendezVous (Date, Heure, IDMedecin, IDSecretaire, IDPatient)
                    VALUES (?, ?, ?, ?, ?)
                ''', (date, heure, medecin, secretaire, patient))

            connection.commit()
            connection.close()
            print("Le rendez-vous a été ajouté à la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'ajout du rendez-vous : {e}")

    @staticmethod
    def Supression(id_rendezvous):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                        DELETE FROM RendezVous WHERE RendezVousID = ?
                    ''', (id_rendezvous,))

            connection.commit()
            connection.close()
            print("Le rendez-vous a été supprimé de la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression du rendez-vous : {e}")

    @staticmethod
    def modifier_rendezvous(id_rendezvous, date, heure, medecin, secretaire, patient):
        try:
            connection = sqlite3.connect('database.sqlite')
            cursor = connection.cursor()

            cursor.execute('''
                    UPDATE RendezVous 
                    SET Date = ?, Heure = ?, IDMedecin = ?, IDSecretaire = ?, IDPatient = ?
                    WHERE RendezVousID = ?
                ''', (date, heure, medecin, secretaire, patient, id_rendezvous))

            connection.commit()
            connection.close()
            print("Le rendez-vous a été modifié dans la base de données avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la modification du rendez-vous : {e}")