from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
#root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def new():
    new_window = customtkinter.CTkToplevel(root, fg_color="white") # Pour créer une nouvelle fénetre
                                                                   # << fg_color="white" >> pour que la couleur de fond soit blanche
    # On definit les attribut titre, dimension, etc... comme on le fait avec une fenetre normale
    new_window.title("fractal")
    new_window.geometry("600x350")
    new_window.resizable(False, True) # Width, Height

    # on definit, la fonction qui vas permettre de fermer le fenetre << new_window >>
    # Remarquons que cette fonction est à l'intérieur de la fonction << new >>
    def close():
        new_window.destroy() # pour fermet la fenetre
        new_window.update()  # pour mettre à jour afin de s'assurer que tout c'est bien passé

    # Bouton de fermeture de la fenetre, remarquez que ce bouton doit etre mis dans la methode << new >>
    # Le premier parametre de ce bouton est << new_window >> car il se met dans la fenetre << new_window >>
    my_button = customtkinter.CTkButton(new_window, text="Close Window", command=close)
    my_button.pack(pady=40)


my_button = customtkinter.CTkButton(root, text="Open New Window", command=new)
my_button.pack(pady=40)

root.mainloop()