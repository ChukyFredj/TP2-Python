from exos import *
from utilitary import *


# Fonction de lancement du menu pour le choix des exercices disponibles
def menu():
    while True:
        print("\n\nListe des exercices du TP1 disponibles :\n")
        print("Exercice 1 > Calcul de Surface")
        print("Exercice 2 > Jeu des allumettes")
        print("Exercice 3 > Les Fichiers")
        print("Exercice 4 > Classe Livre")
        print("Exercice 5 > Classe Roman")
        print("Exercice 6 > Entrer fiche Roman")
        print("0 > Quitter\n")
        choice = verif_1error("Choisissez l'exercice voulu : ")
        print("\n\n\n")
        match choice:
            case 0:
                print("Très bien, au revoir...")
                return
            case 1:
                 exo_1()
            case 2:
                exo_2()
            case 3:
                exo_3()
            case 4:
                exo_4()
            case 5:
                 exo_5()
            case 6:
                 exo_6()
        if not choice_():
            print("Très bien, au revoir...")
            return
