from utilitary import *

import random

def error_cheater(espace,n,nom, m):
    m: int
    toReturn: int
    while m > 3 :
        print("Le maximum qu'on peut retirer est de 3 allumettes",)
        print(" " * (espace), end='')
        print("| " * n, end='')
        m = int(input("{} enlève : ".format(nom)))
        if m <= 0:
            m = error_neg(espace,n,nom, m)
    return m

def error_neg(espace,n,nom, m):
    m: int
    toReturn: int
    while m <= 0 :
        print("Le minimum qu'on peut retirer est 1 allumette",)
        print(" " * (espace), end='')
        print("| " * n, end='')
        m = int(input("{} enlève : ".format(nom)))
        if m > 3:
            m = error_cheater(espace,n,nom, m)
    return m

def exo_2():
    """
    Cette fonction implémente le jeu des allumettes, où deux joueurs (l'utilisateur et l'ordinateur) retirent 1, 2 ou 3 allumettes à tour de rôle.
    Le joueur qui retire la dernière allumette a perdu.
    """

    # Saisie du nom du joueur
    while True:
        nom = input("Entrer votre nom : ")

        # Saisie du nombre d'allumettes de départ
        n = int(input("Choisir le nombre d'allumettes de départ : "))
        espace = 8
        # Détermination aléatoire du joueur de départ
        tour = random.choice([nom, 'ordinateur'])
        print("{} commence".format(tour))

        # Boucle de jeu
        while n > 0:
            # Tour de l'utilisateur
            if tour == nom:
                print(" " * (espace), end='')
                print("| " * n, end='')
                m = int(input("{} enlève : ".format(nom)))
                if m > 3:
                    m = error_cheater(espace,n,nom, m)
                elif m <= 0 :
                    m = error_neg(espace,n,nom, m)
                n -= m
                espace += m *2
                tour = 'ordinateur'

            # Tour de l'ordinateur
            else:
                if n > 3:
                    m = random.randint(1, 3)
                else:
                    m = random.randint(1, n)
                print(" " * (espace), end='')
                print("| " * n, end='')
                print("Ordinateur enlève :", m)
                n -= m
                espace += m *2
                tour = nom

        # Affichage du résultat
        if tour == 'ordinateur':
            print("{} a perdu :-(".format(nom))
            print("L'ordinateur a gagné :-)")
        else:
            print("L'ordinateur a perdu :-(")
            print("{} a gagné :-)".format(nom))
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break
