nom_fichier = input("Quel fichier souhaitez vous lire? ")

try:
    nombre = int(input("Combien de fois doit-on imprimer le fichier? "))
    print(f"Le fichier {nom_fichier} va être imprimé {nombre} fois.")   

    with open(nom_fichier) as fp:
        lines = fp.readlines()
        for n in range(nombre):
            for line in lines:
                print(line.strip())
except ValueError:
    print("Désolé mais vous devez entrer un nombre!") # ce code s'execute si une exception de type "ValueError" est detecter , car on à mentioner "ValueError"
except Exception:
    print("Désolé le fichier en question n'existe pas!") # ce code s'execute si une exception est detecter (peut importe le type de l'exception), car on à mentioner "Exception"
else:
    print("Tout c'est bien passé!") # ce code s'execute si aucune exception n'est detecter
finally:
    print("Ce code s'executera peu importe le résultat du try!") # ce code s'execute dans tous les cas, c'est à dire qu'une exception soit detecter ou pas

print("Merci d'avoir utilisé notre programme.")