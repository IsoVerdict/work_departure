from tkinter import *

fenetre = Tk() # pour créer un objet fenetre
               # on pouvait aussi faire fenetre = tkinter.Tk()

fenetre.geometry("400x400") # pour definir les dimendion de la fenetre
fenetre.title("Ekluz") # pour donner un titre à la fenetre
fenetre["bg"] = "blue" # pour definir la couleur de fond de la fenetre
                       # fenetre.config(background="#FFFFFF")

# fenetre.iconbitmap("images/icon_dual.ico") # pour l'icone de la fenetre

fenetre.resizable(height=False, width=False) # pour dire si on peut ou pas redimensionner la 
                                             # fenetre par rapport à la hauteur(height) ou la largeur(width)

label = Label(fenetre, text = "connexion") # pour créer un label, c'est une zone de texte
label.pack() # pour placer le label au milieu et tout en haut de la fenetre
             # on pouvais aussi faire     << label = Label(fenetre, "connexion").pack() >>     directement

label_2 = Label(fenetre, text = "S'enregistrer", relief=GROOVE) # pour mettre le label en relief
                                                                # les autres options: RAISED, FLAT, SUNKEN, GROOVE, RIDGE
label_2.pack(side = RIGHT, padx = 50) # pour placer le label du coté droit de la fenetre et 
                                      # à partir du coté droit faire n50 pixels vers la gauche

label_3 = Label(fenetre, text = "Neo")
label_3.place(x="12", y="30") # pour placer avec precision dans la fenetre, l'origine du repere ici est le coin 
                              # superieur gauche de la fenetre, plus tu par à droite plus l'abscisse augmente,
                              # plus tu part en bas plus l'ordonnée augmente

label_4 = Label(fenetre, text="Cross", font = ("Verdana", 10, "italic bold"), foreground="white", background="blue")
                              # pour definir la police on utilise font lors de la creation du label
                              # font = (    "le nom de la police"    ,   la taille de la police    ,    quelques effets classic     )
                              # foreground pour la couleur des les lettres, on aurai aussi pu faire fg="white"
                              # bachground pour la couleur de fond, on aurai aussi pu faire bg="blue"

label_4["text"] = "New cross" # pour modifier le texte du label apres l'avoir declarer
label_4.place(x="12",y="50")

fenetre.mainloop()  # pour créer le gestionnaire d'evenement
                    # c'est une sorte de boucle infini dans laquelle il y a tout ce qu'il faut pour afficher la fenetre
