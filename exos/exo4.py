from utilitary import *
from exos.classe.livre import Livre

def exo_4():
    """
    Fonction de test pour la classe Livre
    """
    livre = Livre("Le grand livre du canard gras", "Jean-Baptiste Thiveaud", "Marabout ", "123456789")
    livre.afficher_infos(['nom', 'auteur'])
    livre.modifier_infos(nom="Le canard de Julie", auteur="Julie Andrieu")
    livre.afficher_infos()