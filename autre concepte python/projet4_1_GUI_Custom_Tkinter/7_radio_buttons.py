from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
root.iconbitmap("REP_save_stock/work_departure/images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def get_rad():
    if radio_var.get() == "other":
        my_label2.configure(text="Please Make A Selection")
    elif radio_var.get() == "Yes":
        my_label2.configure(text="Of Course You Like Pizza!")
    else:
        my_label2.configure(text="What's Wrong With You")

my_label = customtkinter.CTkLabel(root, text="Do you Like Pizza?!", font=("Helvetica", 18))
my_label.pack(pady=40)

radio_var = customtkinter.StringVar(value="other")      # c'est la variable qui vas contenir l'information du bouton radio qui a
                                                        # été cliquer on pouvais aussi utiliser << IntVar >> ou autres
my_rad1 = customtkinter.CTkRadioButton(root, text="Yes I Do",
                                       variable=radio_var,      # c'est pour definir la variable qui vas contenir l'information
                                                                # du bouton radio qui a été cliquer
                                       value="Yes",             # l'information du bouton radio qui a été cliquer
                                                                # autrement dit c'est << radio_var >> qui contiendra "Yes" si
                                                                # on clique sur ce bouton 
                                        width=50,   # ceci est la lageur d'un conteneur qui entoure notre bouton radio
                                        height=50,  # ceci est la hauteur d'un conteneur qui entoure notre bouton radio
                                        radiobutton_height=50, # ceci est la vrai hauteur de notre bouton radio
                                        radiobutton_width=50,  # ceci est la vrai largeur de notre bouton radio
                                        corner_radius=1,
                                        border_width_checked=8,   # largeur du bouton après clique
                                        border_width_unchecked=2, # largeur du bouton après clique
                                        border_color="white",     # couleur de la bordure
                                        hover_color="silver",     # couleur du bouton au moment du survole de la souris
                                        fg_color="silver",        # couleur du bouton après clique
                                        hover=True,              # desactiver le survole de la souris
                                        text_color="white",
                                        font=("Helvetica", 18),
                                        state="disableb",           # pour desactiver le bouton, "disableb", "normal", etc...
                                        text_color_disabled="green", # (ça ne marche pas je ne sais pas pouquoi) # pour changer la couleur du texte lorque le bouton est desactiver

                                       )
my_rad1.pack(pady=10)
my_rad1 = customtkinter.CTkRadioButton(root, text="No I Don't",
                                       variable=radio_var,
                                       value="No",
                                       
                                       )
my_rad1.pack(pady=10)

my_label2 = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label2.pack(pady=10)

my_button = customtkinter.CTkButton(root, text="Select", command=get_rad)
my_button.pack(pady=30)

root.mainloop()