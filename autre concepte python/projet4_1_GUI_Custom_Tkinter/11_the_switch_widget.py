from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
#root.iconbitmap('icon_dual.ico') # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

# Create function
def switcher():
    my_label.configure(text=switch_var.get())

# Create Toggle function
def clicker():
    # my_switch.deselect()          # vas deselectionner notre Switch << my_switch >> sans appeler la methode switcher
                                    # donner au paramettre << command= >> donc aura pour effet de ne pas changer le
                                    # texte de notre Label << my_label >>
    
    # my_switch.select()            # vas selectionner notre Switch << my_switch >> sans appeler la methode switcher
                                    # donner au paramettre << command= >> donc aura pour effet de ne pas changer le
                                    # texte de notre Label << my_label >>
    
    my_switch.toggle()              # vas basculer notre Switch << my_switch >> entre l'état selectionner et 
                                    # deselectionner en appelant la methode switcher donner au paramettre 
                                    # << command= >> donc aura pour effet de changer le texte de notre Label << my_label >>

# Create a StringVar
switch_var = customtkinter.StringVar(value="on")
# Create Switch
my_switch = customtkinter.CTkSwitch(root, text="Switch", command=switcher,
                                    variable=switch_var,
                                    onvalue="on",
                                    offvalue="off",
                                    width=50,                          # ceci est la lageur d'un conteneur qui entoure notre Switch
                                    height=50,                         # ceci est la hauteur d'un conteneur qui entoure notre Switch
                                    switch_width=200,                  # ceci est la vrai largeur de notre Switch
                                    switch_height=25,                  # ceci est la vrai hauteur de notre Switch
                                    corner_radius=10,
                                    border_color="orange",             # couleur de la bordure du Switch
                                    border_width=2,                    # largeur de la bordure du Switch
                                    fg_color="red",                    # couleur du Switch lorsque la barre de progression n'est pas encore passé
                                    progress_color="green",            # couleur de la barre de progression
                                    button_color="pink"                # couleur du bouton du Switch
                                    button_hover_color="yellow",       # couleur du bouton du Switch au moment du survole de la souris
                                    font=("Helvetica", 24),
                                    text_color="white",
                                    state="disableb",                  # pour desactiver le Switch, "disableb", "normal", etc...
                                    
                                    )
my_switch.pack(pady=40)

# Create a label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

# Create button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=clicker)
my_button.pack(pady=10)

root.mainloop()