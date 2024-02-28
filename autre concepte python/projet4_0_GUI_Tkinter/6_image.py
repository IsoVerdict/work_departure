from tkinter import *

fenetre = Tk() 

fenetre.geometry("800x800") 
fenetre.title("Ekluz") 
fenetre["bg"] = "blue" 
fenetre.resizable(height=False, width=False)

# PhotoImage ne fonctionne qu'avec les png
photo = PhotoImage(file="images\kind.png") # pour créer une image, plus precisement un objet qui vas contenir une image
label = Label(fenetre, image=photo) # pour mettre notre image dans notre label
label.pack()

fenetre.mainloop()