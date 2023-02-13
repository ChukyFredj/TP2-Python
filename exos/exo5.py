from utilitary import *
from exos.classe.roman import Roman

def exo_5():
    """
    Fonction de test pour la classe Roman
    """
    roman = Roman("Les Misérables", "Victor Hugo", "Hachette", "987654321", "Historique", "Un roman sur la vie des misérables dans la société française du XIXème siècle")
    roman.afficher_infos(['nom', 'auteur', 'type_roman'])
    roman.modifier_infos(nom="Les Misérables de Jean", auteur="Jean Valjean", type_roman="Drame social")
    roman.afficher_infos()

