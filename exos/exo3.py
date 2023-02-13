from utilitary import *

def exo_3():
    """
    Script permettant de créer deux fichiers, un binaire et un texte, qui contiennent chacun 2 entiers saisis au clavier.
    """
    while True:

                # Saisie des entiers pour le fichier binaire
        a_bin = int(input("Entrer le premier entier pour le fichier binaire : "))
        b_bin = int(input("Entrer le deuxième entier pour le fichier binaire : "))

        # Saisie des entiers pour le fichier texte
        a_txt = int(input("Entrer le premier entier pour le fichier texte : "))
        b_txt = int(input("Entrer le deuxième entier pour le fichier texte : "))

        # Ecriture des entiers dans un fichier binaire
        with open('BDD.bin', 'wb') as f:
            f.write(a_bin.to_bytes(4, 'big'))
            f.write(b_bin.to_bytes(4, 'big'))

        # Ecriture des entiers dans un fichier texte
        with open('BDD.txt', 'w') as f:
            f.write(str(a_txt))
            f.write('\n')
            f.write(str(b_txt))

        # Lecture des entiers depuis le fichier binaire
        with open('BDD.bin', 'rb') as f:
            a_bin = int.from_bytes(f.read(4), 'big')
            b_bin = int.from_bytes(f.read(4), 'big')
            print("Données lues depuis le fichier binaire 'BDD.bin' :")
            print(a_bin, b_bin)

        # Lecture des entiers depuis le fichier texte
        with open('BDD.txt', 'r') as f:
            a_txt = int(f.readline().strip())
            b_txt = int(f.readline().strip())
            print("Données lues depuis le fichier texte 'BDD.txt' :")
            print(a_txt, b_txt)
        if input("Voulez-vous continuer ? (o/n) : ") == 'n':
            break
