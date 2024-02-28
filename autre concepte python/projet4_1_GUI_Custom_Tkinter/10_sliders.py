from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def sliding(value):                 # value(on peut la nommé comme on veut) est automatiquement transmise par notre Slider,
                                    # et il faut obligatoirement la mettre entre les parenthèse de la methode qu'on a 
                                    # utilisé dans notre parametre << command= >> de notre Slider
    my_label.configure(text=int(value))  # on pouvais aussi mettre my_slider.get()

my_slider = customtkinter.CTkSlider(root,
                                   from_=0,
                                   to=100,
                                   command=sliding,
                                   orientation="horizontal",
                                   number_of_steps=10,              # nombre d'etapes est en quelques sorte le nombre de fois que le curseur vas se deplacer sur la barre
                                   width=400,
                                   height=50,
                                   border_width=20,
                                   fg_color="red",
                                   progress_color="green",          # couleur de la partie parcouru par le curseur
                                   button_color="yellow",           # couleur du curseur
                                   button_hover_color="orange",     # couleur du curseur lors du survole de la souris
                                   state="normal",                  # etat du Slider "disabled" desactivé, "normal" normal, etc...
                                   hover=False                      # desactiver le survole de la souris
                                   
                                   )
my_slider.pack(pady=40)

# define starting point
my_slider.set(0)


my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18)) # si l'on veut on peut directement mettre my_slider.get()
my_label.pack(pady=20)

root.mainloop()