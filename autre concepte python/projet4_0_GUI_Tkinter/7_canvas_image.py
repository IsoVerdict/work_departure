from tkinter import *

fenetre = Tk()
fenetre.geometry("400x400")
fenetre.title("Ekluz")
fenetre["bg"] = "blue"
# fenetre.iconbitmap("images/icon_dual.ico")

# création du canevas
width = 300
height = 200
can = Canvas(fenetre, width=width, height=height, bg="white")
can.pack()

# recuperation et ajout de l'image
image = PhotoImage(file="images/arch.png").zoom(1) # zoom() c'est pour zoomer, ici c'est x1
can.create_image(width//2, height//2, image=image) # width//2 (la largeur du canvas diviser par deux) et height//2 (la longueur du canvas diviser par deux), sont les coordonnée, 

fenetre.mainloop()