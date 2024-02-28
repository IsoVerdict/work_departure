x = 1                   # Interger
y = 2.5                 # Float
z = -4                  # Integer
a = True                # Boolean
prenom = 'Cedric'       # String
nom = "Midianga"        # String

# On peut declarer plusieurs variables sur une même ligne
variable1, variable2, variable3 = 12, 14.5, "Technique"

# Arithmétiques
print(x + y)            # Addition
print(x neuralnetworkaison
print(x == y)           # Affiche True si x egal à y, sinon affiche False
print(x >= y)           # Affiche True x superieur ou égal à y, sinon affiche False
print(x <= y)           # Affiche True x inferieur ou égal à y, sinon affiche False
print(x != y)           # Affiche True x différent de y, sinon affiche False

# Logique
print(False & True)     # AND
print(False and True)   # AND
print(False | True)     # OR
print(False or True)    # OR
print(not False)        # NOT
print(False ^ True)     # XOR


# Compléments ------------------------------------------------------------------
age = 24
print("Mon âge est:", age, "ans")
taille = 175
print("Ma taille est:", taille, "cm")
#Ceci est un conmmentaire
#Definition de l'age de l'utilisateur
age = 33
print(age)
# Placer le curseur ici et faite << Ctrl + / >>
print("Joyeux anniversaire pour vos", age + 1, "ans")

# Pour connaitre le type d'une variable
age = 24
volume = 2.5
print(type(age))
print(type(volume))

age1 = 4
age2 = 18
total = age1 + age2
print(total)
print(type(total))

volume1 = 3.4
volume2 = 45.152
volumeTot = volume1 + volume2
print(volumeTot)
print(type(volumeTot))

volume3 = 3
volume4 = 45.152
volumeTotal = volume3 + volume4
print(type(volume3))
print(type(volume4))
print(volumeTotal)
print(type(volumeTotal))

rayon = 24.5
pi = 3.14

aire = pi*rayon**2 # où rayon**2 est rayon à la puissance deux
print(aire)
print(type(aire))
# Convertir un angle en degré en radian
# 1 deg = 3.14/180

ratio = 3.14/180
invRatio = 180/3.14
angle_deg = 10
angle_rad = angle_deg*ratio
print(angle_deg, " Degrés = ", angle_rad, " Radians")

angle_rad1 = 5
angle_deg1 = angle_rad1*invRatio
print(angle_rad1, " Radians = ", angle_deg1, " Degrés")

# print("Hello world")
prenom = 'Tom'
print(prenom)

name = "DuBoulevard"
print(name)
print("Je m'appelle", prenom, name)

nombreDeCaracters = len(prenom)
print(nombreDeCaracters)

var1 = "Hello"
var2 = "world"
concatVar = var1 + var2
print(concatVar)
concatVar = var1 +" "+ var2
print(concatVar)
print(type(concatVar))


numb = 100
print(type(numb))
print(type(str(numb)))
# concat = concatVar + numb , est une érreur
concat = concatVar +" "+ str(numb)
print(concat)
print(type(concat))

# Formatage f-string
prenom = "Veronica"
age = 36

texte = "Bonjour je m'appelle " + prenom + " j'ai " + str(age) + " ans." # Methode Classic
print(texte) # Resultat

texte = f"Bonjour je m'appelle {prenom} j'ai {age} ans." # Le formatage f-string
print(texte) # Resultat


# Récuperer les entréesbde l'utilisateur
prenom = input()
print(prenom)

prenom = input("Entrer votre prenom : ")
print("Votre prenom est : ", prenom)


# Une calculatrice : ceci est une erreur car la fonction input renvoi une chaine de caracter, donc il faut convertir en float
    # Erreur
    # nombre_1 = input("Entrer le premier nombre : ")
    # nombre_2 = input("Entrer le deuxième nombre : ")
    # print(type(nombre_1))
    # print(type(nombre_2))
    # # addition
    # print("Addition : ", nombre_1 + nombre_2)
    # # soustraction
    # print("Soustraction : ", nombre_1 - nombre_2)


    # Solution
    nombre_1 = float(input("Entrer le premier nombre : "))
    nombre_2 = float(input("Entrer le deuxième nombre : "))
    print(type(nombre_1))
    print(type(nombre_2))
    # addition
    print("Addition : ", nombre_1 + nombre_2)
    # soustraction
    print("Soustraction : ", nombre_1 - nombre_2)
# --------------------------------------------------------------------


# comditions
tmp0 = 0

if tmp0 > 0:
    print("Positif")
elif tmp0 == 0:
    print("Nul")
else:
    print("Négatif")



# --------------------------------------------------------------------
# L'indentation
username = "Romaric"

if True:
    print("Bienvenue", username)
print("Fin")

if False:
    print("Bienvenue", username)
print("Fin")

if username == "Romaric":
    print("Bienvenue", username)
print("Fin")

varBool = username == "Romaric"
print(varBool)
print(type(varBool))
if varBool:
    print("Bienvenue", username)
print("Fin")

# Une liste
users = ["Stephane", "Alex", "Jackie", "Romaric"] # La liste
print(username in users) # Va retourner True si le contenue de usernamee est dans la liste users
vBool = username in users
if vBool:
    print("Bienvenue", username)
print("Fin")

# Autres conditions et structures de contrôles
prix = 8
if prix > 10:
    print("Le prix est élevé")
else:
    print("C'est un bon prix")
print("Fin")


# Exercice nombre paire ou impaire
nombre = int(input("Entrer un nombre : "))
reste = nombre%2
if reste == 0:
    print(nombre, " est un nombre paire")
else:
    print(nombre, " est un nombre impaire")

# --------------------------------------------------------------------








# --------------------------------------------------------------------
# Boucle for
# On va calculé le carré de chaque element de la liste [0,1,2,3,4,5,6,7,8,9]
tabNum = [0,1,2,3,4,5,6,7,8,9]
for i in tabNum:
    print(f"Le carré de {i} est : {i**2}")

# La fonction range
for i in range(10): # la fonction range permet de generer une sequence de nommbre ici c'est de 0 à 9
    print(i)

tab = range(3, 8) # va generer des nombres de 3 à 7
for i in tab:
    print(i)

tab1 = range(7, 53, 3) # va generer des nombres de 7 à 53 en sautant 3 chiffres : donc 7, 10, 13, 16, 19, 22, etc...
for i in tab1:
    print(i)


# La boucle while
while False: # la boucle n'est pas executer
    print("Dans la boucle")

# while True: # la boucle ne s'arrête jamais
#     print("Dans la boucle")

i=0
while i<=7: # la boucle ne s'arrête jamais
    print("Dans la boucle ", i, " , tour ", i+1)
    i += 1
# --------------------------------------------------------------------















# Tuples
# Un tuple est une liste qu'on ne peut plus modifier apres l'avoir déclarer, et il se déclare avec des parenthèses
un_tuple = ()
deuxieme_tuple = (1, 5, 5.3, 12.45, -5, "bonjour")
numero = (1, 5, 5.3, 12.45, -5)
villes = ("Libreville", "New York", "Tokyo", "Pékin", "Paris", "Sky Land", "Light Sun", "Eternity")

# Structures de donées ou Sequences
# Une sequences est un ensemble d'elements ordonnés, on a: les listes, les tuples, les strings
# Listes
liste_1 = [1, 4, 2, 7, 35, 84]
villes = ['Paris', 'Berlin', 'Londres', 'Bruxelles']
nested_list = [liste_1, villes] # une liste peut meme contenir des listes ! On appelle cela une nested list

#Tuples
tuple_1 = (1, 2, 6, 2)

#String
name = "Harbor Master"

# ---------------------------------------------------------------
# index pour acceder a un elements d'une sequence, c'est à dire liste, tuples ou string
print(villes[0]) # premier element = index 0
print(villes[1]) # deuxieme element = index 1
print(villes[-1]) # dernier element
print(villes[-2]) # avant dernier element



# ---------------------------------------------------------------
# le slicing s'utilise sur les sequence, c'est à dire liste, tuples ou string
# SLICING [début (inclus) : fin (exclus) : pas]
print(villes[0:3]) # affiche le premier (index 0), deuxieme (index 1) et troisieme (index 2) element
print(villes[:3])  # affiche du debut jusqu'au troisieme element (index 2)
print(villes[2:])  # affiche du troisieme element (index 2) jusqu'au dernier élément

print(villes[1:3]) # affiche le deuxieme (index 1) et troisieme (index 2) element

print(villes[1:10:2]) # affiche le deuxieme (index 1) jusqu'au dixieme (index 9) element en fesant un pas de "2" entre chaque element
                      # donc les elements afficher sont : index 1, 3, 5, 7 et 9

print(villes[::2]) # affiche du debut jusqu'à la fin en fesant un pas de "2" entre chaque element

print(villes[::-1]) # affiche du debut à la fin en fesant un pas de "-1" entre chaque element, comme le pas "-1" ramene
                    # en arriere alors, ce sont les elements de la liste villes qui seront afficher en commencant par le 
                    # dernier jusqu'au premier element, c'est à dire la liste sera afficher à l'envers

# methodes sur les liste
villes.append("nouvelle ville") # pour ajouter un element à la fin d'une liste
villes.insert(2, "new city") # pour ajouter un element à l'index 2 d'une liste, 
                             # biensur les elements qui vienne apres celui ci seront decalé par rapport à leur index
villes.extend(une_autre_liste) # pour ajouter une liste à la fin d'une liste

len(villes) # renvoie la taille de la liste villes

villes.sort() # puisque villes est une liste de mots "sort" vas la trier dans l'ordre alphabetique
villes.sort(reverse=True) # vas la trier dans l'ordre anti-alphabetique

liste_1.sort() # puisque liste_1 est une liste de nombre "sort" vas la trier dans l'ordre croissant
liste_1.sort(reverse=True) # dans l'ordre décroissant

villes.count("Paris") # vas renvoyer un nombre, qui est le nombre de fois que "Paris" apparais dans la liste villes
                      # cette methode permet donc de compter le nombre de fois qu'un element apparait dans une liste

villes.clear() # pour vider completement une liste, c'est à dire la liste sera vide [], de taille zero

villes.pop()  # La méthode pop() en Python est une fonction de la classe list qui permet de supprimer un élément d'une liste 
villes.pop(2) # et de renvoyer la valeur de l'élément supprimé. Elle peut prendre un argument optionnel, qui est l'index de l'élément 
              # à supprimer. Si aucun index n'est spécifié, la méthode pop() supprimera et renverra le dernier élément de la liste.


villes.remove() # La commande remove() permet de supprimer un élément repéré par sa valeur dans une liste.
                # Elle supprime le premier élément de la liste ayant cette valeur.

if 'Paris' in villes: # in est comme un operateur pour nous dire si un element est dans une liste
  print('oui')
else:
  print('non')


for element in villes: # pour parcourir les elements de la liste
  print(element)

for index, element in enumerate(villes): # pour parcourir les elements de la liste et leur index
  print(index, element)

for element_1, element_2 in zip(villes, liste_2): # pour parcourir deux liste en même temps, si une 
  print(element_1, element_2)                     # liste est plus courte que l'autre, la boucle for vas 
                                                  # s'arretée lorsqu'elle vas arrivée au dernier élément 
                                                  # de la liste la plus courte



# Les listes comprehension sont une facon habile de créer des listes sur une seule ligne de code, ce qui rend
# le code beaucoup plus rapide (car python est un langage assez lent)
liste = []
for i in range(100000):
  liste.append(i**2)


liste = [i**2 for i in range(100000)] # list comprehension

# On peut rajouter des conditions if dans les listes comprehension, par exemple :
liste = [i**2 for i in range(100000) if (i % 2) == 0] # calcule i**2 seulement pour les nombres pairs.

# les nested list avec les list comprehension, je rappel qu'une nested list (on parle aussi de nested dict pour les dictionnaires) 
# sont des listes qui contiennent des listes (donc par analogie des dictionnaires qui contiennent d'autres dictionnnaires)
liste_3 = [[i for i in range(2)] for j in range(3)]
print(liste_3)

liste_4 = [[i+j for i in range(2)] for j in range(3)]
print(liste_4)


# dictionnaires comprehension
prenoms = ["Pierre", "Jean", "Julie", "Sophie"]
dico = {k:v for  k, v in enumerate(prenoms)} # ce dictionnaires aura pour clée 0, 1, 2 et 3.
                                             # Chaque clée est associée avec le prenom qui était à 
                                             # l'index correspondant à la clée elle même dans la liste prenoms

ages = [24, 12, 54, 48]
dico_2 = {prenom:age for prenom, age in zip(prenoms, ages)} # ce dictionnaire aura pour premiere association clé:valeur
                                                            # "Pierre":24, ensuite "Jean":12, "Julie":54 et "Sophie":48

dico_3 = {prenom:age for prenom, age in zip(prenoms, ages) if age > 30} # ce dictionnaire contient {"Julie":54, "Sophie":48}

# tuples comprehension
tuple_2 = tuple((i**2 for i in range(10))) # pour créer un tuple contenant les carrés de 0 à 9 en une ligne

# en resumé pour les listes, dictionnaires et tuples comprehension il faut faire:
# [   DO this       For this collection       In this situation    ]

# [  Fait ceci     Pour cette collection     Dans cette situation  ]

# [    x**2        for x in range(0, 50)          if x%3 == 0      ]







# --------------------------------------------------------------------
#Listes
ma_liste = [2, 15, 4, 21, 7]
print(type(ma_liste))
print(ma_liste)

villes = ["Paris", "New York", "Londres"]
print(type(villes))
print(villes)

liste_demo = [17, "Paris", 16.5, "Lyon"]
print(type(liste_demo))
print(liste_demo)

# Acceder aux donnees: Indesage et Tranchage
print(len(villes)) # affiche le nombres d'elements de la liste villes
uneVilles = villes[0] # recupere la donnés qui se trouve à l'emplacement zero de la liste villes
print(villes[2])
villes[2] = "Elden Ring" # on a changer la donnés qui se trouve à l'emplacement 2
print(villes[2])
villes[-2] = "New Jersey" # on a changer la donnés qui se trouve à l'emplacement 2
                          # il s'agit ici de l'indexage négatif dans la liste "villes"
                          # si l'on compte en partant de zero de la gauche vers la droites
                          # alors "Paris" vaut 0 , "New York" vaut 1 et "Londres" vaut 2
                          # mais si l'on compte dans le sens inverse alors  "Paris" vaut 0 ,
                          # "New York" vaut -2 et "Londres" vaut -1

print(ma_liste[0:2]) # vas tranche la liste ma_liste de 0 à 1 et vas affiche une liste qui ne contient
                     # que les deux premiere valeur de ma_liste

# Ajouté des élements à une liste
villes.append("Lyon") # permet d'ajouter "Lyon" à la fin de la liste villes
villes.append("New York")
villes.append(73) # on peut ajouter des donner de type differents
print(len(villes))
print(villes)

villes = villes + ["strasbourg", "Libreville"] # vas ajouter cette nouvelle liste à la fin de la liste ville

villes.append("Asie")
villes.append("Europe")
villes.append("Lyon")
print(len(villes))
print(villes)
villes.remove("Asie") # Pour supprimer "Asie" de la liste des villes

villes.remove("Lyon")  # Pour suprimer "Lyon" de la liste mais comme "Lyon"
                       # apparait deux fois se sera seulement le "Lyon" qui est le
                       # plus proche du debut de la liste qui sera supprimer

del villes[5]          # vas supprimer l'élement qui se trouve à l'emplacement 5
del villes[4]

# Operateur d'appartenance : in
varBool1 = "Paris" in villes        # True
varBool2 = "paris" in villes        # False

# Petit exercice
ville = "New York"
if ville in villes:
    print(f"{ville} est déjà dans la liste")
else:
    villes.append(ville)

# Boucle for et liste
for i in [0,1,2,3,4,5,6,7,8,9]:
    print(type(i))
    print(i**2)
    print("Dans la boucle", i)

for v in villes:
    print(v, type(v))
    print(v.upper())        # la methode upper permet de mettre les lettre d'une
                            # chaine de caracter en capital

# Les dictionaires
nom_dictionaire = {clé_1 : valeur_1, clé_2 : valeur_2}
                            # clé_1 et clé_2 peuvent être soit des entiers, des
                            # chaines de caracteres ou des float. Quant à valeur_1
                            # et valeur_2 ils peuvent être de n'importe quel type
                            # de données

achats = {
    "carrottes" : 5.4,
    "lait" : 2.5,
    "oeuf" : 3.4,
    "oranges" : 4.5
    }

print(type(achats))
print(achats)

personne = {
    "nom" : "Dupont",
    "Prenom" : "Benois",
    "age" : 30,
    "marié" : False
}
print(personne)

departements = {
    1: "Ain",
    62: "Pas-de-Calais",
    45: "Loiret"
}
print(departements)

print(personne["nom"])   # vas affiché la valeur qui est à coté de la clé "nom"
print(personne["age"])
print(departements[62])

personne["age"] = 31     # vas modifier la valeur qui est à coté de la clé "age"

achats["bananes"] = 2.3  # vas ajouter la clé "bananes" avec la valeur 2.3 , lorsque
                         # l'on modifie la valeur d'une clé qui n'existe pas elle
                         # est automatiquement ajouté au dictionaire

del achats["oeuf"]       # vas supprimer la clé "oeuf" et sa valeur

unBoolean = "oranges" in achats # on verifie si la clé "oranges" est dans le dictionaire
                                # si oui unBoolean vaut True
# --------------------------------------------------------------------












# --------------------------------------------------------------------------------------------
# Les fonctions de bases de python
# --------------------------------------------------------------------------------------------
a = abs(-3) # la fonction abs() permet de donner la valeur absolue d'un nombre

b = round(2.154) # round() permet d'arrondir par defaut

liste_5 = [2, -5, 45, 12, -16, 50, 61]
maximum = max(liste_5) # max() permet de trouver le maximum
minimum = min(liste_5) # min() permet de trouver le minimum
taille = len(liste_5)  # len() permet de trouver la taille de la liste
somme = sum(liste_5)   # sum() permet de faire la somme de tout les éléments

# 
liste_6 = [True, True, False, True]
all(liste_6) # all() renvoie True si tout les elements de la liste sont egale à True, sinon elle renvoie False
any(liste_6) # any() renvoie True si au moin un des elements de la liste est egale à True, sinon elle renvoie False

# il faut voir que sur des liste numerique un zero << 0 >> est equivaut à False et toute valeur different de zero equivaut à True
liste_7 = [2, -5, 45, 12, -16, 50, 61, 0, 14, 56]
liste_8 = [2, -5, 45, 2, -16, 50, 61, 21, 14, 56]
# donc all() renvoie True si tout les elements de la liste sont non nul, sinon renvoie False. Et any() renvoie True si au moin un 
# element de la liste est non nul, sinon renvoie False
all(liste_7) # ici all vas donc renvoyer False
any(liste_7) # ici any vas donc renvoyer True
all(liste_8) # ici all vas donc renvoyer True
any(liste_8) # ici any vas donc renvoyer True


x = 10
type(x) # pour trouver le type d'une variable
a = str(x) # pour convertir un nombre en chaine de caractere
x = int(a) # pour convertir une chaine de caractere en nombre

y = float(x) # pour comvertir un nombre en float

neo = [1, 2, 5, 8, 4]
tupleNeo = tuple(neo) # pour convertir une liste en tuple
neo = list(tupleNeo) # pour convertir un tuple en liste

a = input("ceci vas etre afficher dans la console") # pour prendre une information entrer par l'utilisateur 
                                                    # sous forme de chaine de caractere

# utilisation de format()
x = 30
ville = "Paris"
message = "La temperature est de {} °C à {}".format(x, ville) # vas remplacer à tour de role dans les 
                                                              # accolades les variable << x >> et << ville >>

# ce code fait exactement la meme chose
message = f"La temperature est de {x} °C à {ville}"


# La fonction open()
# Cette fonction est l'une des plus utile de Python. Elle permet d'ouvrir n'importe quel fichier de votre ordinateur et 
# de l'utiliser dans Python. Différents modes existent :
#
#       le mode 'r' : lire un fichier de votre ordinateur
#       le mode 'w' : écrire un fichier sur votre ordinateur
#       le mode 'a' : (append) ajouter du contenu dans un fichier existant

f = open('text.txt', 'w') # ouverture d'un objet fichier f
f.write('hello')
f.close() # il faut fermer notre fichier une fois le travail terminé

f = open('text.txt', 'r')
print(f.read())
f.close() 

# Dans la pratique, on écrit plus souvent with open() as f pour ne pas avoir a fermer le fichier une fois le travail effectué :
with open('text.txt', 'r') as f:
    print(f.read())

# Exercice et Solution
# Le code ci-dessous permet de créer un fichier qui contient les nombres carrée de 0 jusqu'a 19. L'exercice est d'implémenter 
# un code qui permet de lire ce fichier et d'écrire chaque ligne dans une liste.
#
#     Note_1 : la fonction read().splitlines() sera tres utile
#     Note_2 : Pour un meilleur résultat, essayer d'utiliser une liste comprehension !

# Ce bout de code permet d'écrire le fichier 
with open('fichier.txt', 'w') as f:
    for i in range(0, 20):
        f.write(f'{i}: {i**2} \n')
    f.close()
# Écrivez ici le code pour lire le fichier et enregistrer chaque lignes dans une liste.


# SOLUTION (non optimale)
with open('fichier.txt','r') as f:
    liste = f.read().splitlines()

# SOLUTION (Améliorée)
# Une meilleure facon de procéder est d'utiliser une liste comprehension !
liste = [row.strip() for row in open('fichier.txt','r')]





# --------------------------------------------------------------------
# Fonction
def ma_fonction():               # pour definir une fonction
    print("Bonjour Georges")     # contenue de la fonction

ma_fonction()                    # utilisation de la fonction

# Jeu deviner le nombre
def devinez_le_nombre():
    import random

    selection = random.randint(1,10)

    nombre = 0
    tentatives_max = 5
    tentatives = 0
    while nombre != selection:
        if tentatives >= tentatives_max:
            print("vous avez perdu, le nombre est: ", selection)
            break

        nombre = int(input("Entrez votre nombre: "))

        if selection > nombre:
            print("C'est plus")
        elif selection < nombre:
            print("C'est moins")
        else:
            print("Bravo, vous avez trouvé le nombre")

        tentatives+=1

# devinez_le_nombre()

# Arguments de fonction
def message(user):
    print("Bonjour", user)

message("Cedric")

def aire_cercle(rayon):
    print(f"L'aire de ce cerle est : {3.14*rayon**2}")

aire_cercle(0.5)
aire_cercle(14)

# Utiliser plusieurs arguments
def presentation(prenom, temperature):
    print(f"Bonjour {prenom}")
    print(f"La temperature est de {temperature} °C")

presentation("Tom", 15)
presentation("Jerry", 30)

presentation(15, "Tom")       # vas afficher quelquechose qu'on ne veut pas
presentation(temperature=15, prenom="Tom")       # dans se cas peut importe l'ordre "Tom" et 15 seront
                                                 # afficher au bonne endroit

# Valeur par defaut des arguments
def salutation(prenom = "Tom"):                             # ceci est une valeur par defaut
    print("Bonjour", prenom)

def salut(prenom = "Thomas", temperature = 24):
    print(f"Bonjour {prenom} il fait {temperature} °C.")

salutation()                 # vas afficher "Bonjour Tom"
salut("Eric")

# L'instruction return
def square(nombre):
    return nombre**2
var = 4
squarevar = square(var)
print(f"Le carré de {var} est {squarevar}.")

# Logarithme ratée
def logia(_nombre):
    if _nombre >= 1:
        nombre = _nombre-1
        log_nombre = 0
        signe = 1
        for i in range(1, 99):
            log_nombre += ((nombre**i)/i)*signe
            t = nombre**i
            signe*=(-1)
        return log_nombre
    else:
        return "non definie"

print(logia(2.71828))
# --------------------------------------------------------------------












# --------------------------------------------------------------------------------------------
# Les modules et packages
# --------------------------------------------------------------------------------------------


# Les modules usuels
import math
import statistics
import random
import os
import glob
# Vous pouvez également créer vos propres modules et les importer dans d'autres projets. Un module
# n'est en fait qu'un simple fichier.py qui contient des fonctions et des classes

# 1. Modules math et statistics
# les modules math et statistics sont en apparence tres utiles, mais en data science, nous utiliserons leurs 
# équivalents dans le package NUMPY. Il peut néanmoins etre intéressant de voir les fonctions de bases.
print(math.pi)
print(math.cos(2*math.pi))

liste = [1, 4, 6, 2, 5]
print(statistics.mean(liste)) # moyenne de la liste
print(statistics.variance(liste)) # variance de la liste



# 2. Module Random
# Le module random est l'un des plus utile de Python. En datascience, nous utiliserons surtout sont équivalent NUMPY
random.seed(0) # fixe le générateur aléatoire pour produire toujours le meme résultat
print(random.choice(liste)) # choisit un élément au hasard dans la liste
print(random.random()) # génére un nombre aléatoire entre 0 et 1
print(random.randint(5, 10)) # génére un nombre entier aléatoire entre 5 et 10

random.sample(range(100), 10) # retourne une liste de 10 nombres aléatoires entre 0 et 100

print('liste de départ', liste)
random.shuffle(liste) #mélange les éléments d'une liste
print('liste mélangée', liste)




# 3. Modules OS et Glob
# Les modules OS et GLob sont essentiels pour effectuer des opérations sur votre disque dur, comme ouvrir un fichier 
# situé dans un certain répertoire de travail.
os.getcwd() # affiche le répertoire de travail actuel
print(glob.glob('*')) # contenu du repertoire de travail actuel





# --------------------------------------------------------------------------
# Programmation Orientée Objets
# Créer une class
class Personne: # Le nom d'une class doit commencer par une lettre majuscule
    nom = "Willis"
    prenom = "Bruce"
    age = 65

print(Personne)
print(Personne.nom)

# Créer des objets et les utilliser
bruce = Personne()
alice = Personne()
print(bruce.nom)
print(alice.nom)

# Amelioration
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

bruce = Personne("Hugues", "Bruce", 38)
alice = Personne("Eve", "Alice", 28)

print(bruce.nom, bruce.prenom, bruce.age)
print(alice.nom, alice.prenom, alice.age)
# --------------------------------------------------------------------------