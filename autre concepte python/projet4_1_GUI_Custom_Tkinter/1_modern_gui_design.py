from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
#root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")

my_button = customtkinter.CTkButton(root, text="lets go")
my_button.pack(pady=80)

root.mainloop()