from utilitary import *

def exo_1():
    """
    Script permettant de rentrer 1 caractères et un entier
    Afficher la variables sous forme d'entiers et de caractères
    """

    while True:
        # Définition de la fonction à intégrer
        def f(x):
            return x * x
        # Saisie des variables
        a = float(input("Entrer a : "))
        b = float(input("Entrer b : "))
        p = float(input("Entrer p : "))

        # Initialisation de x et de la surface
        x = a
        area = 0

        # Boucle pour approximer la surface sous la courbe
        while x < b:
            area += f(x) * p
            x += p

        print("Calcul de l’intégrale de la fonction y = x * x")
        print("avec", a, "<= x <", b, "et p =", p)
        print("Résultat {:.3f}".format(area))
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break
