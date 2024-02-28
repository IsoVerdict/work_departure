from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def clicker(value):
    my_label.configure(text=f"Helle {value}") # à la place de "value" on aurai pu utiliser my_seg_button.get()
                                              # mais la methode clicker doit toujour prendre une valeur en 
                                              # parametre qu'on peut nommé comme on veut ici c'est << value >>

# Our button values
my_values = ["John", "April", "Wes"]
# Create the button
my_seg_button = customtkinter.CTkSegmentedButton(root, values=my_values,
                                                 command=clicker,
                                                 width=300,
                                                 height=100,
                                                 font=("Helvetica", 18),
                                                 corner_radius=3,
                                                 border_width=5,
                                                 fg_color="red",
                                                 selected_color="green",             # couleur de l'element selectionné
                                                 selected_hover_color="purple",      # couleur de l'element selectionné lors du survole de la souris
                                                 unselected_color="pink",            # couleur de(s) l'element(s) non-selectionnés
                                                 unselected_hover_color="orange",    # couleur de(s) l'element(s) non-selectionnés lors du survole de la souris
                                                 text_color="yellow",
                                                 state="disabled",
                                                 text_color_disabled="blue",
                                                 dynamic_resizing=True      # redimensionner en fonction de la taille du texte
                                                 )
my_seg_button.pack(pady=40)

# valeur par defaut
my_seg_button.set("John") # Il explique quelque chose d'important video9 5min 00sec


my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)


my_button = customtkinter.CTkButton(root, text="lets go")
my_button.pack(pady=80)

root.mainloop()