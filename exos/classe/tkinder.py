import tkinter as tk
from tkinter import messagebox
from exos.classe.roman import Roman

class Romantkinder(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fiche Roman")

        # Nom
        tk.Label(self, text="Nom").grid(row=0, column=0)
        self.nom_entry = tk.Entry(self)
        self.nom_entry.grid(row=0, column=1)

        # Auteur
        tk.Label(self, text="Auteur").grid(row=1, column=0)
        self.auteur_entry = tk.Entry(self)
        self.auteur_entry.grid(row=1, column=1)

        # Maison d'édition
        tk.Label(self, text="Maison d'édition").grid(row=2, column=0)
        self.maison_edition_entry = tk.Entry(self)
        self.maison_edition_entry.grid(row=2, column=1)

        # Code barre
        tk.Label(self, text="Code barre").grid(row=3, column=0)
        self.code_barre_entry = tk.Entry(self)
        self.code_barre_entry.grid(row=3, column=1)

        # Genre
        tk.Label(self, text="Genre").grid(row=4, column=0)
        self.genre_var = tk.StringVar(value="Policier")
        self.genre_combobox = tk.OptionMenu(self, self.genre_var, "Policier", "Fantastique", "Science-Fiction", "Horreur", "Drame", "Comédie", "Romance", "Autre")
        self.genre_combobox.grid(row=4, column=1)

        # Description
        tk.Label(self, text="Description Roman").grid(row=5, column=0)
        self.description_entry = tk.Text(self, height=5, width=30)
        self.description_entry.grid(row=5, column=1)

        # Bouton sauver
        tk.Button(self, text="Sauver", command=self.sauver).grid(row=6, column=0, pady=10)

        # Bouton fermer
        tk.Button(self, text="Fermer", command=self.destroy).grid(row=6, column=1, pady=10)

    def sauver(self):
        """
        Enregistre les informations saisies dans un fichier
        """
        nom = self.nom_entry.get()
        auteur = self.auteur_entry.get()
        maison_edition = self.maison_edition_entry.get()
        code_barre = self.code_barre_entry.get()
        genre = self.genre_var.get()
        description = self.description_entry.get("1.0", "end-1c")

        roman = Roman(nom, auteur, maison_edition, code_barre, genre, description)

        with open("BDD.txt", "a") as f:
            f.write(f"""
            --------------------
            Nom: {roman.nom}
            Auteur: {roman.auteur}
            Maison d'edition: {roman.maison_edition}
            Code barre: {roman.code_barre}
            Type roman: {roman.type_roman}
            Description: {roman.description_type}
            --------------------
            \n
            """)

        messagebox.showinfo("Confirmation", "Le roman a été sauvegardé.")








