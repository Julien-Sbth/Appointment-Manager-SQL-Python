# main.py
import interface


def main():
    interface.interfaceSecretaire()
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
main()
