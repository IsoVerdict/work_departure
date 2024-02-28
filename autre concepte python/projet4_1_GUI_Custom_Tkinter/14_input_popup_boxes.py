from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
#root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

# Create Function
def input():
    dialog = customtkinter.CTkInputDialog(text="What is your Name?", title="Salut à vous",  # pour créer une boite de dialogue
                                          fg_color="white",
                                          button_fg_color="red",
                                          button_hover_color="pink",
                                          button_text_color="black",
                                          entry_fg_color="green",       # entry c'est la parti ou on entre le texte, sinon à part ça
                                                                        # il est facile de comprendre ce que chaque paramettres fait
                                                                        # à partir de son nom
                                          entry_border_color="red",
                                          entry_text_color="black"
                                          )
    thing = dialog.get_input() # dialog.get_input() pour recevoir ce qui à été saisis dans la boite de dialogue
    if thing:
        my_label.configure(text=f"Salut {thing}") # faire ça si la chaine de caractères << thing >> n'est pas vide
    else:
        my_label.configure(text="Essayez de saisir quelque chose")

# Create a button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=input)
my_button.pack(pady=40)

# Create a label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

root.mainloop()