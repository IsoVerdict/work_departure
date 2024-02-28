from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
# root.iconbitmap("images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

def action_clear():
    my_entry.configure(state="normal")
    my_entry.delete(0, END) # delete( << point de depart du curseur >>, << point d'arriver du curseur >>), ici delete(0, END) signifie que tous sera supprimer
    my_label.configure(text="")
def action_submit():
    my_entry.configure(state="disabled")
    my_label.configure(text=f"Bonjour {my_entry.get()}") # my_entry.get() renvoie le contenue qui a été saisi dans my_entry

my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 24))
my_label.pack(pady=40)

my_entry = customtkinter.CTkEntry(root,
                                  height=50,
                                  width=200,
                                  font=("Helvetica", 18),
                                  corner_radius=50,
                                  text_color="white",
                                  placeholder_text="Enter",         # le texte afficher lorsque qu'il n'y a encore rien d'écris
                                  placeholder_text_color="white",   # changer la couleur du texte afficher lorsque qu'il n'y a encore rien d'écris
                                  fg_color=("white","blue"),        # exterieur, interieur
                                  state="normal"
                                  ) 
my_entry.pack(pady=20)

button_submit = customtkinter.CTkButton(root, text="Submit", command=action_submit)
button_clear  = customtkinter.CTkButton(root, text="Clear", command=action_clear)
button_submit.pack(pady=10)
button_clear.pack(pady=10)

root.mainloop()