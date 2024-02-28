from tkinter import *

fenetre = Tk() 

fenetre.geometry("400x400") 
fenetre.title("Ekluz") 
fenetre["bg"] = "blue" 
fenetre.resizable(height=False, width=False)

# l'interet des boite est de regrouper plusieur objets graphique comme les boutons, labels, etcs... ensemble donc 
# si l'on doit les deplacer ils se deplaceront ensemble
boite = Frame(fenetre, bg="green") # pour créer une boite

label1 = Label(boite, text="Underscore") # pour mettre un label dans la boite nommée << boite >>
label1.pack()
label2 = Label(boite, text="Atlas de carte Ck diff") # idem
label2.pack()

boite.pack(expand=YES) # pour placer la boite au centre de la fenetre
fenetre.mainloop()