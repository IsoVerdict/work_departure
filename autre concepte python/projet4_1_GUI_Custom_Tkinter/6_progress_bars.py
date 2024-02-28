from tkinter import *
import customtkinter

# set the theme and color options
customtkinter.set_appearance_mode("dark") # mode: Systeme (default), dark, light, ...
customtkinter.set_default_color_theme("green") # themes: blue (default), green, drak-bleu, ...

root = customtkinter.CTk()

root.title("fractal")
root.iconbitmap("REP_save_stock\work_departure\images/icon_dual.ico") # on peut aussi faire  root.iconphoto(False, tk.PhotoImage(file='images/icon.png'))
root.geometry("700x250")

def clicker():
    my_progressbar.step()
    my_label.configure( text=str(int((my_progressbar.get()*100)))+"%" )

def start():
    my_progressbar.start()

def stop():
    my_progressbar.stop()

my_progressbar = customtkinter.CTkProgressBar(root, orientation="horizontal",
                                              mode="inderterminate", # ce mode montre une barre avec un curseur qui faite des zig zag entre le debut et la fin
                                                                     # dans le mode "determinate", arriver à la fin la barre recommence au debut
                                              determinate_speed= .05 , # c'est le "pas" d'incrementation diviser par deux en mode "determinate"
                                                                    # pour le nombre à virgule on peut faire  << 1.2 >>
                                                                    # par exemple, et quand c'est << 0 >> avant la virgule
                                                                    # par exemple << 0.4 >> on peut tout simplement faire
                                                                    # << .4 >> cela marche aussi
                                              indeterminate_speed= 2.2, # c'est le "pas" en mode "indetermiate"

                                            height=20,
                                            width=100,
                                            corner_radius=15,
                                            border_width=2,
                                            border_color="white",
                                            fg_color="silver",
                                            progress_color="white", # couleur de la barre de progression
                                              )
my_progressbar.pack(pady=40)

# set the default progress starting point
my_progressbar.set(0) # 0 its 0% and 1 its 100%


my_button = customtkinter.CTkButton(root, text="lets go for +1", command=clicker)
my_button.pack(pady=10)

start_button = customtkinter.CTkButton(root, text="Start", command=start)
start_button.pack(pady=10)

stop_button = customtkinter.CTkButton(root, text="Stop", command=stop)
stop_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="", font=("Helvetica", 18))
my_label.pack(pady=10)

root.mainloop()