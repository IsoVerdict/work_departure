from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
#root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

global thing # une variable 

# Functions
def delete():
    my_text.delete(0.0, "end") # suprimer de la position zero (en flaot) << 0.0 >> jusqu'à la fin << "end" >>

def copy():
    global thing
    thing = my_text.get(0.0, "end") # met dans << thing >> tous ce qui à entre la position zero (en flaot) << 0.0 >> et la fin << "end" >>

def paste():
    global thing
    if thing != "": # si la chaine << thing >> n'est pas vide ce qui suis sera executer, sinon c'est ce qui suis else
        my_text.insert("end", thing) # insert ce qui à dans << thing >> à partir de la fin "end"(on aurai pu aussi mettre une autre position)
    else:
        my_text.insert("end", "There is nothing to paste !!")

my_text = customtkinter.CTkTextbox(root,
                                   width=450,
                                   height=150,
                                   corner_radius=1,
                                   border_width=10,
                                   border_color="#003660",
                                   border_spacing=10, # la marge interieur
                                   fg_color="silver",
                                   text_color="black",
                                   font=("Helvetica", 18),
                                   wrap="word", # Char default, word, none, c'est la manière de couper une ligne lorsqu'elle
                                               # arrive au bord du << Texbox >>
                                   activate_scrollbars=True, # pour activer ou desactiver la scrollbar
                                   scrollbar_button_color="blue",
                                   scrollbar_button_hover_color="red"
                                  )
my_text.pack(pady=20)

# On créer un conteneur dans lequel nous allons mettre nos boutons
my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)

# les boutons on été mis dans << my_frame >>
delete_button = customtkinter.CTkButton(my_frame, text="Delete", command=delete)
copy_button = customtkinter.CTkButton(my_frame, text="Copy", command=copy)
paste_button = customtkinter.CTkButton(my_frame, text="Paste", command=paste)

# nos boutons seront positionner dans << my_frame >>
delete_button.grid(row=0, column=0)
copy_button.grid(row=0, column=1, padx=10)
paste_button.grid(row=0, column=2)

root.mainloop()

# il faut bien voir comment ça fonctionne au niveau de << thing >> il y a des choses à corriger