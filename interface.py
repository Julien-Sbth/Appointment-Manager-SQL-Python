import sqlite3

import RendezVous
from RendezVous.Patients import Patient
from RendezVous.Secretaire import Secretaire


def interfacePatient():
    while True:
        print("1 Pour ajouter un patient")
        print("2 Pour prendre un rendez-vous")
        print("3 Pour modifier un rendez-vous")
        print("4 Pour supprimer un rendez-vous")
        choix = input("Entrez votre choix (ou 'q' pour quitter) : ")

        if choix == "1":
            def ajouter_patient():
                print("Entrez les détails du nouveau patient :")
                Prenom = input("Prenom du patient : ")
                nom = input("Nom du patient : ")
                age = int(input("age du patient : "))
                condition = input("sexe du patient : ")

                nouveau_patient = Patient(Prenom, nom, age, condition)
                nouveau_patient.add_to_database()

            ajouter_patient()

        elif choix == "2":
            print(Patient.AllDisplayDataFromPatient())
            prenom_patient = input("Entrez le prénom du patient à supprimer : ")
            patient_a_supprimer = Patient(prenom_patient, "", 0, "")
            patient_a_supprimer.remove_from_database()
        elif choix == "3":
            Patient.AllDisplayDataFromPatient()

            prenom_a_modifier = input("Entrez le prénom du patient à modifier : ")
            nouveau_nom = input("Entrez le nouveau nom : ")
            nouvel_age = input("Entrez le nouvel âge : ")
            nouveau_sexe = input("Entrez le nouveau sexe : ")

            Patient.Modif_Patient(prenom_a_modifier, nouveau_nom, nouvel_age, nouveau_sexe)
        elif choix == "4":
            pass

        elif choix.lower() == "q":
            break
        else:
            print("Choix invalide. Veuillez entrer un choix valide.")


def interfaceSecretaire():
    print("1 Pour ajouter un secretaire")
    print("2 Pour modifier un secretaire")
    print("3 Pour supprimer un secretaire")
    choix = input("Entrez votre choix (ou 'q' pour quitter) : ")
    if choix == "1":
        def ajouter_secretaire():
            print("Entrez les détails du nouveau secretaire :")
            Prenom = input("Nom du secretaire : ")
            nom = input("Prenom du secretaire : ")
            age = int(input("age du secretaire : "))
            nouveau_secretaire = RendezVous.Secretaire.Secretaire(Prenom, nom, age)
            nouveau_secretaire.add_to_database()

        ajouter_secretaire()

    elif choix == "2":
        def update_secretaire():
            global connection
            try:
                id = int(input("Entrez l'ID du secretaire que vous voulez modifier : "))
                connection = sqlite3.connect('database.sqlite')
                cursor = connection.cursor()

                cursor.execute('SELECT * FROM secretaire WHERE SecretaireId = ?', (id,))
                secretary_data = cursor.fetchone()

                if secretary_data:
                    print("Voici les détails actuels du secretaire :")
                    print(f"ID: {secretary_data[0]}")
                    print(f"Nom: {secretary_data[1]}")
                    print(f"Prenom: {secretary_data[2]}")
                    print(f"Age: {secretary_data[3]}")

                    print("\nEntrez les nouveaux détails du secretaire :")
                    Prenom = input("Nouveau nom du secretaire : ")
                    nom = input("Nouveau prenom du secretaire : ")
                    age = int(input("Nouvel age du secretaire : "))

                    nouveau_secretaire = Secretaire(Prenom, nom, age, id)
                    nouveau_secretaire.update_from_database()

                else:
                    print(f"Aucun secretaire trouvé avec l'ID {id}")

            except ValueError:
                print("Veuillez entrer un ID valide.")

            except sqlite3.Error as e:
                print(f"Erreur lors de la récupération du secretaire : {e}")

            finally:
                if connection:
                    connection.close()

        update_secretaire()
    elif choix == "3":
        def remove_secretaire():
            global connection
            try:
                Secretaire.displayAllData()
                id = int(input("Entrez l'ID du secretaire que vous voulez supprimer : "))
                connection = sqlite3.connect('database.sqlite')
                cursor = connection.cursor()

                cursor.execute('SELECT * FROM secretaire WHERE SecretaireId = ?', (id,))
                secretary_data = cursor.fetchone()

                if secretary_data:
                    print("Voici les détails actuels du secretaire :")
                    print(f"ID: {secretary_data[0]}")
                    print(f"Nom: {secretary_data[1]}")
                    print(f"Prenom: {secretary_data[2]}")
                    print(f"Age: {secretary_data[3]}")

                    confirmation = input("Voulez-vous vraiment supprimer ce secretaire ? (o/n) : ")
                    if confirmation.lower() == "o":
                        secretaire_a_supprimer = Secretaire("", "", 0, id)
                        secretaire_a_supprimer.remove_from_database()

                else:
                    print(f"Aucun secretaire trouvé avec l'ID {id}")
            except ValueError:
                print("Veuillez entrer un ID valide.")
            except sqlite3.Error as e:
                print(f"Erreur lors de la récupération du secretaire : {e}")

            finally:
                if connection:
                    connection.close()

        remove_secretaire()
