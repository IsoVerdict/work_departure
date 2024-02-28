from tkinter import *

fenetre = Tk() 

fenetre.geometry("400x400") 
fenetre.title("Ekluz") 
fenetre["bg"] = "blue" 
fenetre.resizable(height=False, width=False)

def save():
    print("Vous avez cliqué sur le sous onglet \"Enregistrer sous...\" ")

mon_menu = Menu(fenetre) # pour créer un menu

# pour definir des sous onglets
# Sous onglet Fichier
fichier = Menu(mon_menu, tearoff=0) # tearoff=0 permet d'enlever la ligne de traits qui est en haut des sous onglets
fichier.add_command(label="Enregistrer sous...", command=save) # on peut ajouter une commande qui biensur vas faire
                                                               # l'action de la fonction qu'on aura renseigner ici il s'agit de << save >>
# Sous onglet Options
option = Menu(mon_menu)
option.add_command(label="Resolution")

# pour definir les onglets et les liés à leurs sous onglets respectif
# Les 2 principaux onglets
mon_menu.add_cascade(label="Fichier", menu=fichier)
mon_menu.add_cascade(label="Options", menu=option)

fenetre.config(menu=mon_menu) # pour afficher le menu dans la fenetre

fenetre.mainloop()