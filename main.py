# main.py

from RendezVous.Patients import Patient

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
        Patient.AllDisplayDataFromPatient()

        prenom_patient = input("Entrez le prénom du patient à supprimer : ")
        patient_a_supprimer = Patient(prenom_patient, "", 0, "")
        patient_a_supprimer.remove_from_database()
    elif choix == "3":
        Patient.AllDisplayDataFromPatient()

        prenom_a_modifier = input("Entrez l'id du patient à modifier : ")
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
