from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
root.iconbitmap("REP_save_stock\work_departure\images/fractal.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def clear_me():
    my_check.deselect() # << my_check.deselect() >> permet de mettre la case à coché dans l'état "décoché"
    text_var.set("Voulez vous jouez à un jeu ?")

def game():
    if check_var.get() == "on":
        my_label.configure(text="Vous avez coché la case !")
    else:
        my_label.configure(text="Vous n'avez pas coché la case !")
    
    text_var.set("Awesome !!!")

# etat de la case à cocher
check_var = customtkinter.StringVar(value="off") # on pouvait faire value=False, ou value=2, etc... et definir de façon adéquote << onvalue= >> et << offvalue= >>
# texte de la case à cocher
text_var = customtkinter.StringVar(value="Voulez vous jouez à un jeu ?")
my_check = customtkinter.CTkCheckBox(root, text=text_var.get(),
                                     variable=check_var, # la variable qui definie l'etat de la case
                                     onvalue="on", # valeur que doit avoir variable= pour que la case soit dans l'état "coché"
                                     offvalue="off", # valeur que doit avoir variable= pour que la case soit dans l'état "decoché"
                                     checkbox_width=50,
                                     checkbox_height=50,
                                     font=("helvetica", 18),
                                     corner_radius=50,
                                     fg_color="#62F1C5", # vert façons...
                                     hover_color="#02D9E0", # un genre de turquoise...
                                     text_color="green", # couleur du texte
                                     hover=False, # on peut toujours cocher la case mais lorsque la souris vas la survoler il ne vas rien se passer
                                     textvariable=text_var, # pour definir la variable qui vas contenir le texte à coté de la case à cocher
                                     )
my_check.pack(pady=40)

my_button = customtkinter.CTkButton(root, text="Submit", command=game)
my_button.pack(pady=20)

clear_button = customtkinter.CTkButton(root, text="Clear", command=clear_me)
clear_button.pack(pady=10)

toggle_button = customtkinter.CTkButton(root, text="Toggle", command=my_check.toggle()) # on pouvais aussi mettre << my_check.toggle() >> dans une fonction
                                                                                        # << my_check.toggle() >> permet de basculer entre les deux etats de la case à coché
toggle_button.pack(pady=20)

select_button = customtkinter.CTkButton(root, text="Select", command=my_check.select()) # on pouvais aussi mettre << my_check.select() >> dans une fonction
                                                                                        # << my_check.select() >> permet de mettre la case à coché dans l'état "coché"
select_button.pack(pady=20)

# IMPORTANT !!!! select_button et toggle_button force la case à toujours etre coché, il faut trouver une solution

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)

root.mainloop()