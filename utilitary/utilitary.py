# Fonction de choix pour continuer ou pas à faire des exercices
def choice_():
    print("\n\nVoulez-vous essayer un autre exercice ? (O / N)\n> ", end="")
    while True:
        test = input()
        if test in ("O","o"):
            return True
        elif test in ("N","n"):
            return False
        else:
            print("Choisissez une réponse valide !")


# Fonction pour choisir un seul caractère

def verif_2error_float(txt,minval=0,maxval=10000000000000000):
    test: float
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = float(number)
            if test < minval:
                print(f"Vous devez choisir un nombre supérieur a {minval}")
                continue
            if test > maxval:
                print(f"Vous devez choisir un nombre plus petit que {maxval}")
                continue
            break
        except ValueError:
            print("Vous devez choisir un nombre positif (en dessous de 1114111) !")
    return test

# Fonction pour choisir un nombre avec 2 gestions d'erreurs 
def verif_2error(txt,minval=0,maxval=10000000000000000):
    test: int
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = int(number)
            if test < minval:
                print(f"Vous devez choisir un nombre supérieur a {minval}")
                continue
            if test > maxval:
                print(f"Vous devez choisir un nombre plus petit que {maxval}")
                continue
            break
        except ValueError:
            print("Vous devez choisir un nombre positif (en dessous de 1114111) !")
    return test


# Fonction pour choisir un nombre positif avec une gestion d'erreur commune a plein d'exos
def verif_1error(txt,minval=0):
    test: int
    toReturn: int
    while True:
        print(txt, end="")
        number: str = input()
        try:
            test = int(number)
            if minval:
                print("Vous devez choisir un nombre positif !")
                continue
            break
        except ValueError:
            print("Vous devez choisir un nombre positif !")
    return test
