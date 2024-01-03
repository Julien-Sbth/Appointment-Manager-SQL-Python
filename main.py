import interface


def main():
    print("Bienvenue dans le programme de gestion de rendez-vous")
    print("----------------------------------------------------")
    print("Veuillez choisir une option 😊")
    print("1. Rendez-vous")
    print("2. Patient")
    print("3. Médecin")
    print("4. Secrétaire")
    print("5. Quitter")

    choix = input("Votre choix : ")
    if choix == "1":
        interface.interfaceRendezVous()
    elif choix == "2":
        interface.interfacePatient()
    elif choix == "3":
        interface.interfaceMedecin()
    elif choix == "4":
        interface.interfaceSecretaire()
    elif choix == "5":
        print("Merci d'avoir utilisé notre programme")
    else:
        print("Erreur de saisie")
        main()


main()
