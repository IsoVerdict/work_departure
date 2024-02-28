from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
root.iconbitmap("REP_save_stock/work_departure/images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("600x350")


# create a scrollable frame
my_frame = customtkinter.CTkScrollableFrame(root,
                                            orientation="vertical", # orientation de la scrollbar 
                                            width=300,
                                            height=200,
                                            label_text="Hello world!",    # pour mettre du texte à l'en-tête de notre ScrollerFrame
                                            label_fg_color="blue",        # pour changer la couleur de face de l'en-tête de notre ScrollerFrame
                                            label_text_color="yellow",    # pour changer la couleur du texte à l'en-tête de notre ScrollerFrame
                                            label_font=("Helvetica", 10),  # pour changer la police (et taille aussi) du texte à l'en-tête de notre ScrollerFrame
                                            label_anchor= "w",            # "w",  # n(north), ne(north est), e(est), se(sounth est), s(sounth),
                                                                          # sw(sounth west), w(west), nw(north west), center
                                            
                                            border_width=3,               # taille de la bordure du ScrollerFrame
                                            border_color="green",         # couleur de la bordure du ScrollerFrame
                                            fg_color="red",               # couleur de face du ScrollerFrame

                                            scrollbar_fg_color="yellow",            # couleur de face de la scrollbar
                                            scrollbar_button_color="pink",          # couleur de la scrollbar
                                            scrollbar_button_hover_color="blue",     # couleur de la scrollbar lors du survole de la souris
                                            corner_radius=12,                        # le niveau de rondeur des coin du ScrollerFrame
                                            )
my_frame.pack(pady=40)

# for loop for buttons
for x in range(20):
    customtkinter.CTkButton(my_frame, text="This is a Button!!", font=("Helvetica", 10)).pack(pady=10)

my_button = customtkinter.CTkButton(root, text="lets go")
my_button.pack(pady=20)

root.mainloop()