import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title("fractal")
root.geometry("600x350")

def action():
    my_label.configure(text="Vous avez cliqué sur le bouton")

my_canvas = customtkinter.CTkCanvas(root,
                                    width=200,
                                    height=150,
                                    bg="white")
my_canvas.pack(pady=10)

my_button = customtkinter.CTkButton(root, text="lets go", command=action)
my_button.pack(pady=10)

my_label = customtkinter.CTkLabel(root, text="Departure", font=("Helvetica", 18), bg_color="blue") # border_width=2, border_color="blue")
my_label.pack(pady=10)

root.mainloop()