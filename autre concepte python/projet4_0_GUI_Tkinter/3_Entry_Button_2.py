from tkinter import *

fenetre = Tk() # pour créer un objet fenetre
                

fenetre.geometry("400x400") # pour definir les dimendion de la fenetre
fenetre.title("Ekluz") # pour donner un titre à la fenetre
fenetre["bg"] = "blue" # pour definir la couleur de fond de la fenetre
fenetre.resizable(height=False, width=False) # pour dire si on peut ou pas redimensionner la 
                                             # fenetre par rapport à la hauteur(height) ou la largeur(width)

def ma_fonction():
    label["text"] = ma_variable.get()

ma_variable = StringVar()

entree = Entry(fenetre, textvariable=ma_variable) # pour créer une entrée utilisateur, et ce que l'utilisateur aura entrer sera dans la variable << ma_variable >>
entree.pack()

label = Label(fenetre, text="Cross", font = ("Verdana", 10, "italic bold"), foreground="white", background="blue")
label.place(x="12",y="50")

bouton = Button(fenetre, text="connexion", fg="white", bg="blue", command=ma_fonction) 
bouton.pack() 

fenetre.mainloop() # pour créer une boucle infini dans laquelle il y a tout ce qu'il faut pour afficher la fenetre