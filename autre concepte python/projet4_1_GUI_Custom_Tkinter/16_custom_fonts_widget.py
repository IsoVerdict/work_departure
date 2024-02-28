from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
#root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def change():
    # on met à jour certain paramettre de la police
    my_font.configure(underline=False, overstrike=False, size=22, slant="roman")

# si l'on créer une police de la manière dont nous l'avons toujours fait avec l'atribut << font=... >>
# on ne pourra pas changer la police de façons dynamique (c'est à dire pendant l'exécution du programme)
# pour se faire il faut proceder comme ce qui suit, utiliser << my_font >> dans le parametre font de 
# notre Label (ou Button, etc...) et mettre à jour cette police avec la methode << configure >>
# par exemple dans une fonction ici << change >> qui sera relié à un bouton qu'on aura créer ici << my_button >>
my_font = customtkinter.CTkFont(family="Helvetica", size=44, weight="bold", slant="italic",
                                underline=True, overstrike=True) # weight="bold" ou "normal",   stant="italic" ou "roman"

my_label = customtkinter.CTkLabel(root, text="This is Text", font=my_font)
my_label.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Change Text", command=change)
my_button.pack()

root.mainloop()