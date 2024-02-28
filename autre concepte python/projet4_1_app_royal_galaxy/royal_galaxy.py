import customtkinter
import dynamicneuralnetwork.d2n_math
import dynamicneuralnetwork.d2n_neuralnetwork

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title("Royal Galaxy")
root.geometry("1500x1300")


def generer_une_fractal():
    pass

def effacer():
    pass

def clear_button():
    pass

def generer():
    pass

button_frame = customtkinter.CTkFrame(root)
button_frame.grid(row=0, column=0, padx=5)

entry_frame = customtkinter.CTkFrame(root)
entry_frame.grid(row=1,column=1)

my_canvas = customtkinter.CTkCanvas(root, height=900, width=1700, bg="ivory")
my_canvas.grid(row=0, column=1)


# pour dessiner un réseau de neurones
my_network=dynamicneuralnetwork.d2n_neuralnetwork.Nnr(450, 0, [4, 5, 3])
my_network.drawall(my_canvas)

# pour dessiner une couche
my_stack=dynamicneuralnetwork.d2n_neuralnetwork.Stack(240, 0, 5)
my_stack.drawall(my_canvas)


# pour dessiner un neuronne et ses branches
ner1=dynamicneuralnetwork.d2n_neuralnetwork.Neurone(0, 420, mode="L")
ner1.draw(my_canvas)

# un autre neuronne
ner2=dynamicneuralnetwork.d2n_neuralnetwork.Neurone(0, 280, color="blue", mode="R")
ner2.draw(my_canvas)





# on place la barre d'enter et le bouton supprimer dans le << entry_frame >>
equation_input = customtkinter.CTkEntry(entry_frame, 
                                        placeholder_text="Saisisser une équation", 
                                        height=30, 
                                        width=670, 
                                        font=("Helvetica", 18))
clear_button = customtkinter.CTkButton(entry_frame, 
                                       text="X", 
                                       height=30, 
                                       width=30, 
                                       fg_color="red", 
                                       hover_color="grey", 
                                       font=("Helvetica", 18), 
                                       command=clear_button)
equation_input.grid(row=0, column=0, sticky="W")
clear_button.grid(row=0, column=1, sticky="E")

my_button0 = customtkinter.CTkButton(button_frame, text="Générer une fractal", command=generer_une_fractal)
my_button1 = customtkinter.CTkButton(button_frame, text="Effacer", command=effacer)
my_button2 = customtkinter.CTkButton(button_frame, text="Générer", command=generer)
my_button0.grid(row=0, pady=3)
my_button1.grid(row=1, pady=3)
my_button2.grid(row=2, pady=3)

root.mainloop()