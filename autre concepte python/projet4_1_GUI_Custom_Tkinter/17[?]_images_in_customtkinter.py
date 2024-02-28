from tkinter import *
import customtkinter
from PIL import Image # pour utiliser les images c'est en quelque sorte la meillieur pratique
# from PIL import ImageTk

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
root.geometry("600x400")

# il est plus facile de redimentionner les images avec << CustomTkinter >> le faire avec << Tkinter >> normal est plus compliquer
my_image = customtkinter.CTkImage(light_image=Image.open("images/arch.png"), # il n'y pas vraiment de différence apparente entre dark et light
                                  dark_image=Image.open("images/arch.png"),  # mais vous pouvez utilisé les deux en même temps ou light lorsque 
                                                                             # votre fenetre est en mode light (theme light) et dark pour le
                                                                             # theme dark 
                                  size=(360,300) # pour la taille de l'image (redimentionner l'image), si on ne mentionne rien alors l'image sera très petite
                                  )

my_label = customtkinter.CTkLabel(root, text="", image=my_image)
my_label.pack(pady=10)

root.mainloop()

# une erreur c'est produite, voir ça après