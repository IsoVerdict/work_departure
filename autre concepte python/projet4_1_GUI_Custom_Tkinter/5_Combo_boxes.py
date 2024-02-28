from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...
root = customtkinter.CTk()
root.title("fractal")
# root.iconbitmap("images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

# FUNCTIONS -----------------------------------------------------------------------------------------------------------------------------
def color_picker(choice): # combobox vas créer un evenement à chaque fois qu'on clique sur un choix 
                          # de la liste deroulante, nous allons appeler ici cet evenement << choice >>
                          # ici << choice >> vas contenir la chaine de caractere de la couleur sur laquelle on a cliqué
    output_label.configure(text=choice, text_color=choice)

def color_picker2():
    output_label.configure(text=my_combo.get(), text_color=my_combo.get()) # my_combo.get() renvoie une chaine de caracteres
                                                                           # qui permet non seulement d'afficher
                                                                           # le nom de la couleur << text=my_combo.get() >> et
                                                                           # de changer aussi la couleur << text_color=my_combo.get() >>
def color_picker_yellow():
    my_combo.set("Yellow") # ici "Yellow" ne sera pas ajouter à la liste des couleurs, 
                           # "Yellow" sera juste la valeur de << my_combo.get() >>, avant qu'une action comme
                           # "cliquer sur une couleur de la liste deroulante" ou "utiliser le bouton << my_button >>
                           # que nous avant definis plus bas" change à nouveau la valeur de << my_combo.get() >>
    output_label.configure(text=my_combo.get(), text_color=my_combo.get())


my_label = customtkinter.CTkLabel(root, text="Pick A Color", font=("Helvetica", 18))
my_label.pack(pady=40)

# Set the options for our combobox
colors = ["Red", "Green", "Blue"]
# Create combobox
my_combo = customtkinter.CTkComboBox(root, values=colors, #, command=color_picker) # si l'on garde cette commande alors que color_picker2 est là, 
                                                                                  # alors on aura un petit sousis mais pas trop grave
                                                                                  # en faite elle change prematuremment le texte de << output_label >>
                                            height=50,
                                            width=200,
                                            font=("Helvetica", 18),
                                            dropdown_font=("Helvetica", 18),
                                            corner_radius=50,
                                            border_width=2,                     # taille bord interieur
                                            border_color="red",                 # couleur bord interieur
                                            button_color="red",                 # couleur du bouton permettant d'afficher la liste deroulante
                                            button_hover_color="green",         # couleur du bouton permettant d'afficher la liste deroulante au moment du survole de la souris
                                            dropdown_hover_color="green",       # couleur des elements de la liste deroulante au moment du survole de la souris
                                            dropdown_fg_color="blue",           # couleur de face des elements de la liste deroulante
                                            dropdown_text_color="orange",       # couleur du texte des elements de la liste deroulante
                                            text_color="silver",                # couleur du texte de l'element choisi
                                            hover=True,                         # permet de dire si l'on change ou pas la couleur du bouton permettant d'afficher la liste deroulante au moment du survole de la souris
                                            justify="center",                   # comme dans microsoft office... pour le texte de l'element choisi
                                            state="normal"                      # Pour definir l'etat de la liste deroulant, normal, ou desactivé, etc...
)
my_combo.pack(pady=0)


# BUTTONS ------------------------------------------------------------------------------------
# Create a button
my_button = customtkinter.CTkButton(root, text="Pick A Color", command=color_picker2)
my_button.pack(pady=0)

#Yellow button
yelloow_button = customtkinter.CTkButton(root, text="Pick Yellow", command=color_picker_yellow)
yelloow_button.pack(pady=20)

# Create output label
output_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
output_label.pack(pady=20)





root.mainloop()


# video5, 9min 10sec