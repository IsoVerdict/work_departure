# SYNTAXE: widget.grid(options)

# Voici la liste des options possibles :

# column : La colonne dans laquelle placer le widget; 0 par défaut (colonne à gauche).
# columnspan : Combien de colonnes le widget occupe; par défaut 1.
# ipadx, ipady : Combien de pixels pour remplir le widget, horizontalement et verticalement, à l’intérieur des bordures du widget.
# padx, pady : Combien de pixels pour remplir le widget, horizontalement et verticalement, à l’extérieur des bordures du widget.
# row : La ligne dans laquelle placer le widget; par défaut la première ligne qui est encore vide.
# rowpan : Combien de lignes le widget occupe; par défaut 1.
# sticky : Que faire si la cellule est plus grande que le widget. sticky peut être la concaténation de chaîne de zéro ou plus de N, E, S, W, NE, NW, SE et SW.
 

# Exemple:

from tkinter import *
gui = Tk()
Label(gui, text="Firstname").grid(row=0)
Label(gui, text="Lastname").grid(row=1)
e1 = Entry(gui)
e2 = Entry(gui)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
gui.mainloop()