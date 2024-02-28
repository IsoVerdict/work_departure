from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
# root.iconbitmap("images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def hello():
    print("hello world")
    my_label.configure(text="Whatever") # c'est defferent de tkinter normal, ceci vas changer l'attribut text de my_label
    my_label2.configure(text=my_button.cget("text")) # ceci vas changer l'attribut text de my_label2 en "ltes go" qui est l'attribut text de my_button

my_button = customtkinter.CTkButton(root,
                                    text="letsython go",
                                    command=hello,
                                    height=100,
                                    width=200,
                                    font=("Helvetica", 24),
                                    text_color="black",
                                    fg_color="yelow",
                                    corner_radius=50,           # pour definir à quel point le bord du bouton sont arrondis
                                    bg_color="blue",            # couleur de l'arrière plan
                                    border_width=10,            # taille de la bordure
                                    border_color="yellow",      # couleur de la bordure
                                    state="normal")             # etat du bouton, "normal" le bouton se comporte normalement, 
                                                                # "disabled" le bouton ne fait rien lorqu'on clique sur lui ou lorsqu'on le survol
                                 
my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)

my_label2 = customtkinter.CTkLabel(root, text="")
my_label2.pack(pady=30)


root.mainloop()from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
# root.iconbitmap("images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def hello():
    print("hello world")
    my_label.configure(text="Whatever") # c'est defferent de tkinter normal, ceci vas changer l'attribut text de my_label
    my_label2.configure(text=my_button.cget("text")) # ceci vas changer l'attribut text de my_label2 en "ltes go" qui est l'attribut text de my_button

my_button = customtkinter.CTkButton(root,
                                    text="letsython go",
                                    command=hello,
                                    height=100,
                                    width=200,
                                    font=("Helvetica", 24),
                                    text_color="black",
                                    fg_color="ythonius=50,           # pour definir à quel point le bord du bouton sont arrondis
                                    bg_color="blue",            # couleur de l'arrière plan
                                    border_width=10,            # taille de la bordure
                                    border_color="yellow",      # couleur de la bordure
                                    state="normal")             # etat du bouton, "normal" le bouton se comporte normalement, 
                                                                # "disabled" le bouton ne fait rien lorqu'on clique sur lui ou lorsqu'on le survol
                                 
my_button.pack(pady=80)

my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=20)

my_label2 = customtkinter.CTkLabel(root, text="")
my_label2.pack(pady=30)


root.mainloop()