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
        pass
    elif choix == "3":
        pass
    elif choix == "4":
        pass

    elif choix.lower() == "q":
        break
    else:
        print("Choix invalide. Veuillez entrer un choix valide.")
