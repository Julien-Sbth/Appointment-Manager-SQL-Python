import sqlite3

from RendezVous.PrendreRendezVous import RendezVous

try:
    conn = sqlite3.connect('database.sqlite')
    print("Connexion réussie!")

    cursor = conn.cursor()


    Patient = ('Alice', 30, 'test')

    cursor.execute("INSERT INTO Patient (Prenom, Nom, Age) VALUES (?, ?, ?)", Patient)

    conn.commit()

    cursor.close()
    conn.close()
except sqlite3.Error as e:
    print("Erreur lors de la connexion à la base de données:", e)

while True:
    while True:
        print("1 Pour prendre un rendez-vous")
        print("2 Pour modifier un rendez vous")
        print("3 Pour supprimer un rendez-vous")
        choix = input("Entrez votre choix (ou 'q' pour quitter) : ")

        if choix == "1":
            RendezVous.prendre_rendezvous()  # Définit par sa date, son heure, le patient concerner  le nom du
            # médecin, la secrétaire qui enregistre le rendez-vous
        elif choix == "2":
            RendezVous.Modification()
        elif choix == "3":
            RendezVous.Supression()
        elif choix == "q":
            print("au revoir")
        break

