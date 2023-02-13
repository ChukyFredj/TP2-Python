from exos.classe.livre import Livre

class Roman(Livre):
    """
    Classe représentant un roman qui hérite de la classe Livre avec les propriétés suivantes :
    type_roman : str
    description_type : str
    """
    def __init__(self, nom, auteur, maison_edition, code_barre, type_roman, description_type):
        """
        Constructeur de la classe Roman
        """
        Livre.__init__(self, nom, auteur, maison_edition, code_barre)
        self.type_roman = type_roman
        self.description_type = description_type

    def afficher_infos(self, infos_a_afficher=None):
        """
        Affiche les informations sur le roman
        """
        Livre.afficher_infos(self, infos_a_afficher)
        if infos_a_afficher is None:
            infos_a_afficher = ['type_roman', 'description_type']
        if 'type_roman' in infos_a_afficher:
            print("Type de roman :", self.type_roman)
        if 'description_type' in infos_a_afficher:
            print("Description du type de roman :", self.description_type)

    def modifier_infos(self, type_roman=None, description_type=None, nom=None, auteur=None, maison_edition=None, code_barre=None):
        """
        Modifie les informations sur le roman
        """
        Livre.modifier_infos(self, nom, auteur, maison_edition, code_barre)
        if type_roman:
            self.type_roman = type_roman
        if description_type:
            self.description_type = description_type
