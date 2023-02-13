class Livre:
    """
    Classe représentant un livre avec les propriétés suivantes :
        nom : str
        auteur : str
        maison_edition : str
        code_barre : str
    """

    def __init__(self, nom, auteur, maison_edition, code_barre):
        """
        Constructeur de la classe Livre
        """
        self.nom = nom
        self.auteur = auteur
        self.maison_edition = maison_edition
        self.code_barre = code_barre

    def afficher_infos(self, infos_a_afficher=None):
        """
        Affiche les informations sur le livre
        """
        if infos_a_afficher is None:
            infos_a_afficher = ['nom', 'auteur', 'maison_edition', 'code_barre']
        if 'nom' in infos_a_afficher:
            print("Nom du livre :", self.nom)
        if 'auteur' in infos_a_afficher:
            print("Auteur :", self.auteur)
        if 'maison_edition' in infos_a_afficher:
            print("Maison d'édition :", self.maison_edition)
        if 'code_barre' in infos_a_afficher:
            print("Code barre :", self.code_barre)

    def modifier_infos(self, nom=None, auteur=None, maison_edition=None, code_barre=None):
        """
        Modifie les informations sur le livre
        """
        if nom:
            self.nom = nom
        if auteur:
            self.auteur = auteur
        if maison_edition:
            self.maison_edition = maison_edition
        if code_barre:
            self.code_barre = code_barre