from tkinter import *

fen = Tk()

fen.geometry("400x400")
fen.title("Ekluz")
fen["bg"] = "blue"
# fen.iconbitmap("images/icon_dual.ico")
fen.resizable(height=False, width=False)

# une fonction "callback" est une fonction passé en argument d'une autre fonction,
# on ecris juste le nom de la fonction sans arguments ni parenthese.

#------------------------------------------------------------------------------------------------------------------------------------------------
# ajout du canevas à la fenetre
width_can = 300
height_can = 200
can = Canvas(fen, width=width_can, height=height_can, bg="ivory")
can.grid(row=1, columnspan=4, padx=20, ipady=20)

'''
# fonction qui permet de tracer une croix au centre du canevas
def create_croix():
    ligne1 = can.create_line(width_can//2-5, height_can//2-5, width_can//2+5, height_can//2+5, fill="black", width=5) # create_line(x0, y0, x1, y1, fill="couleur", width=epaisseur)
    ligne2 = can.create_line(width_can//2-5, height_can//2+5, width_can//2+5, height_can//2-5, fill="black", width=5) # (x0, y0) coordonnée du point de depart de la ligne
                                                                                                                      # (x1, y1) coordonnée du point d'arrivée
'''
# tracer une croix au centre du canevas
ligne1 = can.create_line(width_can//2-5, height_can//2-5, width_can//2+5, height_can//2+5, fill="black", width=5) # create_line(x0, y0, x1, y1, fill="couleur", width=epaisseur)
ligne2 = can.create_line(width_can//2-5, height_can//2+5, width_can//2+5, height_can//2-5, fill="black", width=5) # (x0, y0) coordonnée du point de depart de la ligne
                                                                                                                  # (x1, y1) coordonnée du point d'arrivée

#------------------------------------------------------------------------------------------------------------------------------------------------




# fonctions pour les actions des boutons
def bouger_haut(event):
    '''deplacer la croix de 5pts vers le haut'''
    can.move(ligne1, 0, -5)
    can.move(ligne2, 0, -5)

def bouger_bas():
    '''deplacer la croix de 5pts vers le bas'''
    can.move(ligne1, 0, +5)
    can.move(ligne2, 0, +5)

def bouger_gauche():
    '''deplacer la croix de 5pts vers la gauche'''
    can.move(ligne1, -5, 0)
    can.move(ligne2, -5, 0)

def bouger_droite():
    '''deplacer la croix de 5pts vers la droite'''
    can.move(ligne1, +5, 0)
    can.move(ligne2, +5, 0)

def tracer_cercle():
    '''trace un cercle à la position actuelle du curseur'''
    # recuperation de la liste x0, y0, x1, y1 de la croix
    coordo = can.coords(ligne1)
    # création d'un cercle correspondant à la croix
    can.create_oval(coordo[0]-5, coordo[1]-5, coordo[2]+5, coordo[3]+5, outline="red", width=1)
    # changement de couleur de croix
    can.itemconfig(ligne1, fill="blue")
    can.itemconfig(ligne2, fill="blue")
'''
def clear(event):
    # suprimer tout ce qui à été dessiner
    can.delete(ALL)
    # recréer et redessiner la croix
    ligne1 = can.create_line(width_can//2-5, height_can//2-5, width_can//2+5, height_can//2+5, fill="black", width=5)
    ligne2 = can.create_line(width_can//2-5, height_can//2+5, width_can//2+5, height_can//2-5, fill="black", width=5)
'''

# can.delete(nom): suprimr l'item nom passé en paramètre (ou tous les 
# items si utilisation de ALL à la place de nom)
# can.itemconfig(nom, param): modifie le ou les paramètres spécifiés de
# l'item nom
# can.itemcget(nom, param): retourne la valeur actuelle du paramètre
# param de l'item nom
'''   
if can.itemcget(ligne1, "fill") == "blue":
    can.itemconfig(ligne1, fill="black")
'''

# .bind() est un fonction qui permet de dire ce qu'il faut 
# faire pour les evenements clavier et souris
# L'evenement est enfermé entre des chevrons <...> par exemple <Button-1> correspond
# au bouton 1 de la souris (le bouton de gauche)

# fonction qui vas gerer un clic droit de la souris
def clic_souris(event):
    '''Gestion du clic droit de la souris'''
    # event.x et event.y contiennent les coordonnées du clic effectué
    # création d'un cercle correspondant à la croix
    can.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, outline="green", width=2)

# Attente du clic droit de la souris
can.bind("<Button-3>", clic_souris)

'''
# attente de l'action sur la touche supprimer () juste en haut de la touche entrer
fen.bind("<KeyPress-c>", clear)
'''

# attente de l'action sur la touche Up du clavier
fen.bind("<KeyPress-Up>", bouger_haut) # comme on a appeler bouger_haut ici on peut mettre le paramettre "event" la ou on a definit cette fonction.


# Tkinter permet de combiner différents évènements:
# <Button-1>: l'utilisateur a appuyé sur le premier bouton de la souris (celui de gauche)
# Double : indique qu'un evenement s'est produit 2 fois dans un court laps de temps.
# Par exemple, <Double-Button-1> indique un double clic sur le bouton gauche de la souris
# <KeyRelease-A> : l'utilisateur a relaché la touche A.
# <Control-Shift-KeyPress-B> : l'utilisateur a appuyé simultanément sur
# les touches Ctrl, Maj et B.




# Ajout du bouton haut
boutonH = Button(fen, text="Haut", command=bouger_haut)
boutonH.grid(row=2, column=1, pady=5)
# Ajout du bouton bas
boutonB = Button(fen, text="Bas", command=bouger_bas)
boutonB.grid(row=3, column=1, pady=5)
# Ajout du bouton gauche
boutonG = Button(fen, text="Gauche", command=bouger_gauche)
boutonG.grid(row=2, rowspan=2, column=0)
# Ajout du bouton droite
boutonD = Button(fen, text="Droite", command=bouger_droite)
boutonD.grid(row=2, rowspan=2, column=2)
# Ajout du bouton tracer
boutonT = Button(fen, text="Tracer", command=tracer_cercle)
boutonT.grid(row=2, column=3)
# Ajout du bouton quiter
boutonQ = Button(fen, text="Quiter", command=fen.destroy)
boutonQ.grid(row=3, column=3)



fen.mainloop()