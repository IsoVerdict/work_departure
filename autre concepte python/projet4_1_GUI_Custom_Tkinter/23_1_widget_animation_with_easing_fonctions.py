from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root = Tk()
root = customtkinter.CTk()

root.title('Tkinter.com - CustomTkinter Widget Animations')
# root.iconbitmap('images/codemy.ico')
root.geometry('700x450')

def ease_out_bounce(x): # Animation avec easing fonction
    n1 = 7.5625
    d1 = 2.75

    if (x < 1 / d1):
        return n1 * x * x
    elif (x < 2 / d1):
        x_tmp = x
        x -= 1.5
        return n1 * (x / d1) * x_tmp + 0.75
    elif (x < 2.5 / d1):
        x_tmp = x
        x -= 2.25
        return n1 * (x / d1) * x_tmp + 0.9375
    else:
        x_tmp = x
        x -= 2.625
        return n1 * (x / d1) * x_tmp + 0.984375
    

global step # mal codé
step = 450/2+350

global my_y # mal codé
my_y = 450/2+350

def up(): # mal codé
    global my_y
    global step
    my_y = int(ease_out_bounce(step))
    step -= 2
    if my_y >= 195:
        my_text.place(x=700/2, y=my_y, anchor='center')
        up_button.configure(text=my_y)
        root.after(10, up) # pour dire de réexecuter cette fonction << up >> après 2 millisecondes

def down(): # mal codé
    global my_y
    global step
    my_y = int(ease_out_bounce(step))
    step += 2
    if my_y <= 750:
        my_text.place(x=700/2, y=my_y, anchor='center')
        up_button.configure(text=my_y)
        root.after(10, down) # pour dire de réexecuter cette fonction << down >> après 2 millisecondes


# Frame
my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=20)

# Buttons
up_button = customtkinter.CTkButton(my_frame, text="Up", command=up)
up_button.grid(row=0, column=0, padx=10)

down_button = customtkinter.CTkButton(my_frame, text="Down", command=down)
down_button.grid(row=0, column=1, padx=10)

# Text Box 
my_text = customtkinter.CTkTextbox(root, width=400, height=200)
my_text.place(x=700/2, y=my_y, anchor='center')



root.mainloop()

# c'est mal codé, il y a des bugs