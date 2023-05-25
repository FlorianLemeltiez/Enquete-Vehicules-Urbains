from Vehicules import Vehicules, GestionnaireVehicules

if __name__ == "__main__":
    gestionnaire = GestionnaireVehicules()

    while True:
        print("1. Ajouter un véhicule")
        print("2. Supprimer un véhicule")
        print("3. Modifier un véhicule")
        print("4. Afficher les véhicules")
        print("0. Quitter")

        choix = int(input("Choix : "))

        if choix == 1:
            gestionnaire.ajouter_vehicule()
        elif choix == 2:
            gestionnaire.supprimer_vehicule()
        elif choix == 3:
            gestionnaire.modifier_vehicule()
        elif choix == 4:
            gestionnaire.afficher_vehicules()
        elif choix == 0:
            break
        else:
            print("Choix invalide. Réessayer.\n")
