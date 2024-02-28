from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


root = customtkinter.CTk()

root.title('Tkinter.com - Object Oriented CustomTkinter')
# root.iconbitmap('images/codemy.ico')
root.geometry('700x450')

def clear():
	my_text.delete('0.0', END)

# Text Box
my_text = customtkinter.CTkTextbox(root, width=600, height=300)
my_text.pack(pady=20)

my_button = customtkinter.CTkButton(root, text="Clear Box", command=clear)
my_button.pack(pady=20)

root.mainloop()