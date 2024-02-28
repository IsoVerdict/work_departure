# Exercice 1:
# a = 23
# b = 0
# resultat = a/b

# Exercice 2:
# tableau = ['a', 'b']
# print(tableau[2])

# Exercice 3:
# nombres = {
#        1: "un",
#        2: "deux"
#    }
# print(nombres[3])


# ----------------------------------------------------------------------------------
# Exercice 4:
# nom = "test.txt"
# f = open(nom, 'r')

# Correction:
nom = "test.txt"

try:
    f = open(nom, 'r')
    print(f.read())
except FileNotFoundError:
    print("Le fichier n'existe pas!") # ce code s'execute si une exception de type 
                                      # "FileNotFoundError" est detecter , car on à 
                                      # mentioner "FileNotFoundError"
except:
    print("Oups une erreur s'est produite!") # ce code s'execute si une exception 
                                             # est detecter (peut importe le type 
                                             # de l'exception),on peut aussi le 
                                             # faire en mentionnant "Exception" 
                                             # tout court
finally:
    f.close()
    print("Le fichier est bien fermé!") # ce code s'execute dans tous les cas, 
                                        # c'est à dire qu'une exception soit 
                                        # detecter ou pas
# ----------------------------------------------------------------------------------


# Exercice 5:
# texte = "a"
# int(texte)

# ----------------------------------------------------------------------------------
# Pour créer une exception il faut créer une classe qui portera le nom de 
# l'exception que vous voulez créer, biensur vous pouvez choisir ce nom comme bon 
# vous semble
class DiscoNotAllowedException(Exception): # il faut en suite que cette classe herite de la classe Exception

    def __init__(self):
        super().__init__("Vous n'avez pas le droit d'entrer!") # ceci est le message afficher dans la cosole si l'exception n'est pas gérer

def entrerEnDisco(age):
    if age > 18:
        print("Bienvenu")
    else:
        raise DiscoNotAllowedException() # ceci declare l'exception, c'est à dire que l'instruction "raise DiscoNotAllowedException()" declance l'exception

if __name__ == "__main__":

    entreEnDisco(20)
    try:
        entrerEnDisco(15)   # vu la façons dont on a créer la fonction entrerEnDisco, il est claire que ce code vas generer une Exception
    except DiscoNotAllowedException: # ici on gere l'exception
        print("Désolé vous n'avez pas le droit d'entrer car vous êtes mineur") # et c'est le message qui est afficher lorsque l'exception est gerer
    entreEnDisco(34)
# ----------------------------------------------------------------------------------