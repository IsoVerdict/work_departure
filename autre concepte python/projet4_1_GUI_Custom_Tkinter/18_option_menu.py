from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter OptionMenu')
# root.iconbitmap('images/icon_dual.ico')
root.geometry('700x450')

#Create function
def color_picker(choice):   # choice est un évènement qui contient l'élément selectionné,
                            # cette methode est appelé lorsque l'on utilise la commande command=color_picker
                            # comme vous le voyez color_picker et color_picker2 font exactement la même chose
                            # nous avons choisi de garder le bouton pick_button qui appel color_picker2
                            # et de mettre en commentaire la commande command=color_picker qui appele color_picker
	my_label.configure(text=choice, text_color=choice)

def color_picker2():
	my_label.configure(text=my_option.get(), text_color=my_option.get()) # my_option.get() renvoie l'élément sélectionné

def yellow():
	my_option.set("Yellow") # permet de changer l'element selectionné, on peut meme mentionner quelque chose qui n'est pas sur la liste
	my_label.configure(text=my_option.get(), text_color=my_option.get())	

# Set the options for our OptionMenu
colors = ["Red", "Green", "Blue"]

# Create OptionMenu
my_option = customtkinter.CTkOptionMenu(root, values=colors,
	#command=color_picker)
	height=50,
	width=200,
	font=("Helvetica", 18), # police de la zone montrant l'élément selectionné
	fg_color="white",
	dropdown_font=("Helvetica", 18), # police des éléments de la liste deroulante
	corner_radius=50,
	button_color="red",
	button_hover_color="green",
	dropdown_hover_color="green",
	dropdown_fg_color="blue",
	dropdown_text_color="orange",
	text_color="red",
	hover=True,
	anchor="center", # n-s-e-w-center
	state="normal",
	text_color_disabled="black",
	dynamic_resizing=False, 
	)
	

my_option.pack(pady=40)


my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(pady=10)

pick_button = customtkinter.CTkButton(root, text="Make Choice", command=color_picker2)
pick_button.pack(pady=10)

yellow_button = customtkinter.CTkButton(root, text="Pick Yellow", command=yellow)
yellow_button.pack(pady=10)
root.mainloop()