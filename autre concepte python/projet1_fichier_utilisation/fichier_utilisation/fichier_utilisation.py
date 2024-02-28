open("students.txt", "+w") # vas ouvrir le fichier students.txt qui doit être dans le meme dossier que le fichier de ce script, si le fichier students.txt n'existe pas alors il sera créer mais ne contiendra rien

file = open("students.txt", "+w") # cela permet de recuper une sorte d'objet qui vas nous permetre d'effectuer des action sur notre fichier students.txt
file.write("Paul") # pour ecrire dans le fichier, mais la methode write ne revien pas à la ligne apres avoir ecris quelque chose, pour revenir à la ligne il faut ecrir \n, comme ci-apres
file.write("Edouard\n") # le \n c'est pour faire un saut de ligne
file.write("Elodie")
file.close() # pour fermé le fichier

with open("students.txt", "w+") as file: # le mot clé "with" permet de recuperer le contexte de quelque chose en python ici c'ext le fichier que vas retourné la fonction open(), et ensuite le mot clé "as" permet de nommer ce contexte, donc ici de nommer la variable (ou instance d'objet) qui vas contenir ce fichier
    file.write("Pauline\n")
    file.write("Gwendal\n")
    file.close()

with open("students.txt", "a+") as file: # le mot clé "a+" permet decrir à la suite de ce qui est de ja present dans le fichier, mais le mot clé "w+" avait pour effet d'ecraser se qui est dans le fichier avant ecriture (ou autre chose)
    file.write("Pauline\n")
    file.write("Gwendal\n")
    file.close()

students_list = ["Mathieu", "paul", "Elie", "Jean", "Gilbert", "Thomas", "Clement"]
with open("students.txt", "a+") as file: 
    for student in students_list:
        file.write(student+"\n")
    file.close()


import os
import random

if os.path.exists("students.txt"):
    with open("students.txt", "r+") as file:
        students_list = file.readline()
        print(students_list)
        students_random_choice = random.choice(students_list)
        print("Félicitation à vous: ", students_random_choice)
        file.close()
else:
    print("Le document n'existe pas ! attention !")


#    import os
#    import shutil
#
#    source = "eagle-icon.png" # c'est l'emplacement actuel du fichier
#    target = "images/nouveau_nom.png" # destination de notre fichier que l'on a stocké dans une variable, "nouveau_nom.png" est le nom que la copie aura 
#
#    shutil.copy(source, target) # pour copier le fichier mentionner par source dans la destination mentionner par target
#    os.remove(source) # pour suprimer le fichier mentionner par source

