# Il est conseillé de développer ses applications Tkinter en utilisant 
# une classe (voir POO)

# Une classe crée un espace de noms propre à votre application, et toutes 
# les variables nécessaires seront des attributs de cette classe. Cela 
# facilitera leur utilisation lors des actions sur votre GUI.

# Cela présente l'avantage d'encapsuler l'application de manière 
# efficace et d'éviter ainsi l'utilisation de variables globales 
# (à proscrire pour éviter les effets de bord).


# -------------------------------------------------------------------------------
# CE QU'IL FAUT FAIRE
''' Une application graphique qui donne le nombre d'occurrence d'un nom
'''
# -------------------------------------------------------------------------------


# import bibliotheque Tkinter
from tkinter import *
# on crée notre appliction en tant que classe
class Application(Tk):
    # constructeur
    def __init__(self):
        Tk.__init__(self)
        # Options de la fenêtre
        self.title("NSI4Noobs - Exemples tkinter")
        self.geometry("400x300")
        self.iconbitmap("images/baby-kraken-yellow.ico")
        self.config(bg="#CCCCCC")
        self.resizable(width=True, height=True)

        # DEFINITION DES ATTRIBUTS
        # Dimension zone graphique
        self.width_graphe=750
        self.height_graphe=500
        # Créer les variables de saisie et initialisation
        self.prenom = StringVar()
        self.prenom.set("")
        # Couleur
        self.vals = ["red", "green", "blue"]
        self.etiqs = ["rouge", "vert", "bleu"]
        self.varGr = StringVar()
        # Valeur par defaut
        self.varGr.set(self.vals[1])
        # Texte afficher
        self.txt_choixprenom = StringVar()
        self.txt_choixprenom.set("Zone de résultat")


        # AJOUT DES WIDJETS
        # Ajouter les titres
        self.creer_titres()
        # Ajouter Zone saisie
        self.creer_saisie()
        # Ajouter Zone Graphique
        self.creer_zone_graphique()
        # Ajouter les boutons
        self.creer_boutons()

        # Gestion des évènements sur la fenêtre principale
        self.bind("<Escape>", self.destroy)
        self.bind("<KeyPress-Return>", self.recherche)

    self.choix_prenom = Entry(self.frame_prenom, width=50, textvariable=self.prenom)
    self.choix_prenom.grid(row=0, column=1)

    def creer_titres(self):
        pass

    def recherche(self):
        # Action Si clic sur bouton Rechercher ou appui sur Entrée
        txt = self.prenom.get().upper().strip()
        couleur = self.varGr.get()
        if prenom_existe(txt):
            self.label_graphe.config(fg="#000000")
            self.txt_choixprenom.set("Etude du prénom "+txt)
            generer_graphe(txt, couleur)
    
    def creer_boutons(self):
        # Methode de création et positionnement des boutons sur la fenêtre principale
        ## Ajout du bouton rechercher
        self.button = Button(self, text="Rechercher", bg="#DEE5DC", bd=2, command=self.recherche)
        self.button.pack(expand=YES)
        # Bouton Quitter
        self.boutonQ = Button(self, text="Quitter", command=self.destroy)
        self.buttonQ.pack(expand=YES)
    
    def creer_saisie(self):
        pass

    def creer_zone_graphique(self):
        # Créer la zone de graphique
        # Zone de graphique
        self.frame_graphe = Frame(self, relief=GROOVE, borderwidth=2, width=self.width_graphe, height=self.height_graphe)
    

if __name__ == "__main__":
    app = Application()
    app.mainloop()