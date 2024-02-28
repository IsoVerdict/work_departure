from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
#root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def clicker():
    my_button.configure(text="You Clicked The Tab Button")

# Create Tabview
my_tab = customtkinter.CTkTabview(root,
    width=600,                                        # largeur du TabView
    height=250,                                       # hauteur du TabView
    corner_radius=10,
    fg_color="silver",                                # couleur du TabView
    segmented_button_fg_color="red",                  # couleur d'arriere plan des onglets du TabView
    segmented_button_selected_color="green",          # couleur de l'onget selectionner
    segmented_button_selected_hover_color="pink",     # couleur de l'onget selectionner lors du survole de la souris
    segmented_button_unselected_color="yellow",       # couleur de(s) l'onget(s) non selectionner
    segmented_button_unselected_hover_color="purple", # couleur de(s) l'onget(s) non selectionner lors du survole de la souris
    text_color="red",
    state="normal",                                   # "disable", etc...
    command=clicker                                   # la methode << clicker >> vas etre executer à chaque fois qu'on clique
                                                      # sur un onglets 
                                  )
my_tab.pack(pady=10)

# Create tabs
tab_1 = my_tab.add("Tab N°1")
tab_2 = my_tab.add("Tab N°2")

# Put stuff in tabs
my_button = customtkinter.CTkButton(tab_1, text="Click Me !")
my_button.pack(pady=40)

root.mainloop()