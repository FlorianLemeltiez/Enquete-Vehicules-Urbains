import sys

class Vehicules:
    def __init__(self, marque, modele, annee, couleur):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
    
    def afficher_informations(self):
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Couleur :", self.couleur)

class GestionnaireVehicules:
    def __init__(self):
        self.vehicules = []

    def ajouter_vehicule(self):
        marque = input("Marque : ")
        modele = input("Modèle : ")
        annee = input("Année : ")
        couleur = input("Couleur : ")
        
        vehicule = Vehicules(marque, modele, annee, couleur)
        self.vehicules.append(vehicule)
        
        print("Véhicule ajouté\n")

    def supprimer_vehicule(self):
        if not self.vehicules:
            print("Aucun véhicule à supprimer.")
            return
    
        marque_recherchee = input("Marque du véhicule : ")
        modele_recherche = input("Modèle du véhicule : ")
        annee_recherche = input("Année du véhicule : ")
        couleur_recherche = input("Couleur du véhicule : ")
    
        vehicule_trouve = None
    
        for vehicule in self.vehicules:
            if vehicule.marque == marque_recherchee and vehicule.modele == modele_recherche and vehicule.modele == annee_recherche and vehicule.modele == couleur_recherche:
                vehicule_trouve = vehicule
                break
    
        if not vehicule_trouve:
            print("Véhicule non trouvé.")
            return
    
        self.vehicules.remove(vehicule_trouve)
    
        print("Véhicule supprimé \n")


    def modifier_vehicule(self):
        if not self.vehicules:
            print("Aucun véhicule à modifier.")
            return
    
        marque_recherchee = input("Marque du véhicule : ")
        modele_recherche = input("Modèle du véhicule : ")
        annee_recherche = input("Année du véhicule : ")
        couleur_recherche = input("Couleur du véhicule : ")
    
        vehicule_trouve = None
    
        for vehicule in self.vehicules:
            if vehicule.marque == marque_recherchee and vehicule.modele == modele_recherche and vehicule.modele == annee_recherche and vehicule.modele == couleur_recherche:
                vehicule_trouve = vehicule
                break
    
        if not vehicule_trouve:
            print("Véhicule non trouvé.")
            return
    
        marque = input("Nouvelle marque : ")
        modele = input("Nouveau modèle : ")
        annee = input("Nouvelle année : ")
        couleur = input("Nouvelle couleur : ")
    
        vehicule_trouve.marque = marque
        vehicule_trouve.modele = modele
        vehicule_trouve.annee = annee
        vehicule_trouve.couleur = couleur
    
        print("Véhicule modifié \n")
        
        
    def afficher_vehicules(self):
        if not self.vehicules:
            print("Aucun véhicule à afficher.")
            return
        
        print("Liste des véhicules :")
        
        for i, vehicule in enumerate(self.vehicules):
            print(f"Véhicule {i+1}:")
            print(f"Marque : {vehicule.marque}")
            print(f"Modèle : {vehicule.modele}")
            print(f"Année : {vehicule.annee}")
            print(f"Couleur : {vehicule.couleur}")

        


if __name__ == "__main__":
    Vehicules01 = Vehicules("Citroen", "C3", 2002, "Vert")
    Vehicules02 = Vehicules("Citroen", "C4", 2007, "Bleu")
    Vehicules03 = Vehicules("Renault", "Clio", 2012, "Gris")
    Vehicules04 = Vehicules("Peugeot", "206", 2003, "Jaune")
    Vehicules01.afficher_informations()