from tkinter import *

fenetre = Tk()
fenetre.geometry("400x400")
fenetre.title("Ekluz")
fenetre["bg"] = "blue"
fenetre.iconbitmap("images/icon_dual.ico")

# variable de control 
# Une variable de controle de Tkinter est un objet special qui 
# se comporte comme une variable ordinaire de python: c'est un
# conteneur pour valeur comme un nombre ou une chaine de caractères
# Eles peuvent être partagées entre plusieurs widgets (label, frame,
# buttom, etc...), et elles se souviennent de tous les wiggets qui
# les partagent à un moment donné

# on accede au contenu de la variable avec .get()
# on affecte une valeur à une variable avec .set()

# pour créer:
# un float c'est DoubleVar() par defaut contient 0.0
# un int IntVar() c'est par defaut contient 0
# un string StringVarc'est par defaut contient la chaine de caractere vide ""

# tout les widgets relié à une variable de controle sont automatiquement mis à jour quand une
# variable est modifiée quand la boucle sera à nouveau atteinte avec mainloop()

def si_clic_bouton():
    txt_bouton.set("vous avez deja cliqué sur le bouton")

# texte du bouton
txt_bouton = StringVar()
txt_bouton.set("mon bouton")

# definition du bouton
mon_bouton = Button(fenetre, 
                    textvariable=txt_bouton,
                    bg="#DEE5DC",
                    bd=2,
                    command=si_clic_bouton)

# positionnement du bouton
mon_bouton.place(x=50, y=20)

fenetre.mainloop()