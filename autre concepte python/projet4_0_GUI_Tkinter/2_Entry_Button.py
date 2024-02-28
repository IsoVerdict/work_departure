from tkinter import *

fenetre = Tk() # pour créer un objet fenetre

fenetre.geometry("400x400") # pour definir les dimendion de la fenetre
fenetre.title("Ekluz") # pour donner un titre à la fenetre
fenetre["bg"] = "blue" # pour definir la couleur de fond de la fenetre
fenetre.resizable(height=False, width=False) # pour dire si on peut ou pas redimensionner la 
                                             # fenetre par rapport à la hauteur(height) ou la largeur(width)

def ma_fonction():
    print("connecter")

bouton = Button(fenetre, text="connexion", fg="white", bg="blue", command=ma_fonction) # pour créer un bouton
                                                    # il faut voir que l'attribut << command >> permet de definir l'action que 
                                                    # vas faire le bouton apres qu'on est cliquer sur lui.
                                                    # là le bouton (après le click) vas faire ce que la fonction << ma_fonction >> fait
bouton.pack() # pour placer un bouton dans la fenetre

ma_variable = StringVar() # il ne faut pas faire ma_variable = "" ça peut créer des erreurs
entree = Entry(fenetre, textvariable=ma_variable) # pour créer une entrée utilisateur, et ce que l'utilisateur
                                                  # aura entrer sera dans la variable << ma_variable >>
entree.pack()

fenetre.mainloop() # pour créer une boucle infini dans laquelle il y a tout ce qu'il faut pour afficher la fenetre