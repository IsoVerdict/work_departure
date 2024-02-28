from tkinter import *

fenetre = Tk()
fenetre.geometry("400x400")
fenetre.title("Ekluz")
fenetre["bg"] = "blue"
fenetre.iconbitmap("images/icon_dual.ico")

# valeurs des puces
vals = ["red", "green", "blue"]

# etiquettes des puces
etiqs = ["rouge", "vert", "bleu"]

# variable de memorisations du choix de l'utilisateur "couleur"
varCouleur = StringVar()

# valeur par defaut = la seconde = indice 1
varCouleur.set(vals[1])

# remplissage des boutons radio
for i in range(3):
    boutons = Radiobutton(fenetre,
                          variable=varCouleur,
                          text=etiqs[i],
                          value=vals[i],
                          bg="#CCCCCC")
    boutons.pack(side=LEFT, expand=1) 

fenetre.mainloop()