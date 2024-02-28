# Les fonctions de type mathématique
f = lambda x: x**2 # Equivaut à dire f(x)=x^2
print(f(3)) # vas afficher 9

g = lambda x, y: x**2 + y**2 + y/3 + 2*x + 4 # Equivaut à dire g(x)=x^2 +y^2 +y/3 +2x +4
print(g(1,0)) # vas afficher 7

# Les autres fonctions
# voici une fonction qui ne fait rien et lorsque l'on ne veut rien mettre dans une fonction on mais la seul instruction "pass"
def rien_du_tout():
    pass

# voici une fonction qui double la valeur passer en parametre
def une_fonction(a):
    tmp = a
    a *= 2
    print(f"le nombre {tmp} a été doublé")
    return a

# une autre fonction
def bonjour(nom, age=18, taille=1.80):
    print(f"Bonjour {nom}, tu as {age} ans et une taille de {taille} m.")

# encore deux autres fonctions
def add(a, b):
    resultat =  a + b
    print(f"{a} + {b} = {resultat}")
    return resultat

def sub(a, b):
    resultat =  a - b
    print(f"{a} - {b} = {resultat}")
    return resultat

bonjour("Jean", taille=2.1)
print(f"Le resultat de add(3,4) = {add(3,4)}")
print(f"Le resultat de sub(10,4) = {sub(10,4)}")

print(bonjour) # etant donné que "bonjour" écrit sans parenthèse "bonjour()" designe une fonction le résultat de ce print vas dire qu'il s'agit d'un objet de type function

a = bonjour # comme bonjour est un objet de type function, alors on peut stocker cette objet dans une variable "a" par exemple
a("Paul", taille=1.8) # puis l'utiliser comme on l'aurai fait avec la fonction bonjour

# un decorateur est une fonction qui prend en parametre une autre fonction ("func" par exemple) qui adapte son comportement est executant du code avant ou apres l'exution de la fonction en question ("func") et renvoie une nouvelle fonction
# on un decorateur est utiliser pour :
#       *ajouter du code recurrent (comme du logging, le temps d'execution d'une fonction,etc...)
#       *controle d'accès
#       *caching
#       *vérification de paramètres (verifier les parametres passés a une fonction)
#       *traiter des exceptions

# voici des decorateurs dont le comoprtement est assez intuitif à comprendre

# deco_01
def deco_01(func):
    return func("Alex")

deco_01(bonjour) # on utilise le décorateur sur la fonction bonjour

# deco_02
def deco_02(func):
    return func(12, 4)

deco_02(add) # il est claire que deco_02 ne peut etre utilisé sur 
             # la fonction bonjour car dans le fonctionnement de 
             # deco_02 retourne une fonction qui prend en 
             # parametre 12 et 4 (func(12, 4)), ce qui n'est pas 
             # conforme car la fonction bonjour est faite pour 
             # prendre aobligatoirement un parametre nom et deux 
             # autre parametres optionels
deco_02(sub)



# deco_03
def deco_03(func): # ce decorateur contient une fonction "ajouter_log" qui utilise la fonction passé en paramètre "func" 

    def ajouter_log():
        return func(12, 4)
    
    return ajouter_log # et renvoie la la fonction "ajouter_log"

a = deco_03(add) # donc a et b sont des objet de type function et auront le comportement de "ajouter_log"
b = deco_03(sub)
print(a) # vas afficher que a et b sont des objet de type function
print(b)

print(a()) # vas afficher le resultat de add(12, 4)
print(b()) # vas afficher le resultat de sub(12, 4)



# deco_04
def deco_04(func): # ce decorateur est une modification du decorateur deco_03 

    def ajouter_log():
        print(f"Avant la fonction {func.__name__}") # l'attribut __name__ permet d'avoir le nom de la fonction
        resultat = func(12, 4)
        print(f"Après la fonction {func.__name__}")
        return resultat
    
    
    return ajouter_log # et renvoie la la fonction "ajouter_log"

a = deco_04(add) # donc a et b sont des objet de type function et auront le comportement de "ajouter_log"
b = deco_04(sub)

print(a) # vas afficher que a et b sont des objet de type function
print(b)

print(a()) # vas afficher le resultat de add(12, 4) avec les modifications du decorateur
print(b()) # vas afficher le resultat de sub(12, 4) avec les modifications du decorateur

# c'est là que ça devient intérêssant, au lieu de mettre le resultat de deco_04 dans de nouvelle variable a et b 
# on aurai pu mettre le resultat sur une variable qui porte le même nom que la variable passer en parametre de 
# deco_04 comme ceci "add = deco_04(add)" et "sub = deco_04(sub)" (on rappel qu'ici add et sub sont des objets 
# de type function). Dans ce cas, si on utilise à nouveau les fonction add ou sub elles vont s'executer avec le 
# nouveau comportement decris dans le decorateur "deco_04", en gros c'est comme si on avait << FAIT UNE DECORATION >>
# et il sufit juste de faire "add = deco_04(add)" ou pas pour que la décoration s'applique ou pas.

add = deco_04(add)
sub = deco_04(sub)

# De plus python nous permet de de faire simplement cette decoration en mentionnant @deco_04 juste avant la definition de 
# de la fonction à decorer, nous allons le montrer avec d'autre exemple. Mais il faut savoir que dans ce cas le decorateur
# doit être definit avant la fonction à decorer



# deco_05
def deco_05(func): # ce decorateur est une modification du decorateur deco_04 

    def ajouter_log():
        print(f"New trick !!! Avant la fonction {func.__name__}") # l'attribut __name__ permet d'avoir le nom de la fonction
        resultat = func(12, 4)
        print(f"New trick !!! Après la fonction {func.__name__}")
        return resultat
    
    
    return ajouter_log # et renvoie la la fonction "ajouter_log"

@deco_05
def calcul(a, b):
    resultat =  3*a + 7*b
    print(f"3 x {a} + 7 x {b} = {resultat}")
    return resultat

print(calcul()) # l'on remarque aussi qu'il n'y a pas d'erreur alors que l'on n'a pas donné de parametre 
                # a la fonction "calcul"
@deco_05
def salut(nom, age=18, taille=1.80):
    print(f"Salut {nom}, tu as {age} ans et une taille de {taille} m.")

# print(salut("Cedric")) # vas donner une erreur car notre decorateur "deco_05" à en sont sein une fonction "ajouter_log"
                       # qui ne prend rien en parametre, en effet "salut" ici est en faite "ajouter_log" il faut donc modifier
                       # le comportement de "ajouter_log" dans notre decorateur, pour ça on vas ajouter deux parametres
                       # à "ajouter_log" *args et **kwargs qui sont respectivement un tableau de tous les parametres positionel
                       # et un dictionnaire de tous les parametres optionel (Donc etant donné un éléments du dictionnaire
                       # la clé sera le nom du parametre, et la valeur associée à cette clé sera la valeur par defaut du parametre )
                       # nous alons faire tous ça dans un nouveau decorateur



# deco_06
def deco_06(func): # ce decorateur est une modification du decorateur deco_05

    def ajouter_log(*args, **kwargs):    # *args et **kwargs qui sont respectivement un tableau de tous les parametres positionel
                                         # et un dictionnaire de tous les parametres optionel (Donc etant donné un éléments du dictionnaire
                                         # la clé sera le nom du parametre, et la valeur associée à cette clé sera la valeur par defaut du parametre )
        print(f"New trick !!! Avant la fonction {func.__name__}") # l'attribut __name__ permet d'avoir le nom de la fonction
        resultat = func(*args, **kwargs)
        print(f"New trick !!! Après la fonction {func.__name__}")
        return resultat
    
    
    return ajouter_log # et renvoie la la fonction "ajouter_log"

@deco_06
def lineaire(a, b):
    resultat =  7*a + 10*b
    print(f"7 x {a} + 10 x {b} = {resultat}")
    return resultat

@deco_06
def hello(nom, age=18, taille=1.80):
    print(f"Hello {nom}, tu as {age} ans et une taille de {taille} m.")

print(hello("Cedric"))
print(lineaire(4, 5))

print(hello.__name__)       # vas afficher le nom de la fonction "ajouter_log" malheureusement
print(lineaire.__name__)    # pour remedier à ça il faut ajouter un decorateur existant déjà dans python 
                            # qu'il faudrat importer en fesant "from functools import wraps" qui a la 
                            # particularité de prendre en parametre une fonction, et qui sera dans notre cas 
                            # la fonction dont on veux garder le nom. Nous allons illustrer ça avec un autre
                            # decorateur.



# deco_07
from functools import wraps
def deco_07(func): # ce decorateur est une modification du decorateur deco_06

    @wraps(func) # ceci permet de garder le vrai nom de la fonction qui a subit une decoration
                 # il faut l'importer en fesant "from functools import wraps"
                 # une question se pose << Comment créer un decorateur qui prend quelque chose en parametre? >>
                 # Nous allons illustrer ça avec deux autres decorateurs.
    def ajouter_log(*args, **kwargs):
        print(f"New trick !!! Avant la fonction {func.__name__}")
        resultat = func(*args, **kwargs)
        print(f"New trick !!! Après la fonction {func.__name__}")
        return resultat
    
    
    return ajouter_log # et renvoie la la fonction "ajouter_log"

@deco_07
def interGalactik():
    pass

print(interGalactik())
print(interGalactik.__name__)



# repeter et deco_08
def repeter(nbr_iterations):
    def decorateur(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            resultat = []
            for i in range(nbr_iterations):
               resultat.append(func(*args, **kwargs))
            
            return resultat # nous somme entrain de retourner un tableau de fonction, ce qui aura pour effet 
                            # d'afficher les elements des print des fonctions, ce comportement est illustré 
                            # quelques lignes plus bas
        
        return wrapper
    
    return decorateur
# en procedant de cette facons l'on vien de créer un decorateur repeter qui prend en parametre
# le nombre de fois qu'il vas repeter une fonction

@repeter(3)
def allGalactik():
    print("Un message de signalement !!!")

print(allGalactik.__name__)
allGalactik() # vas afficher trois fois le message "Un message de signalement !!!" car nous
              # avons appliquer le decorateur repeter(3) (avec 3 en parametre)



# comportement d'une tableau de fonctions, on a nommé ce tableau "t"
def allmind():
    print("all mind")

def allcraft():
    print("all craft")

def totalcraft(c):
    a=10
    b = c + 10*a
    print(f"total craft {b}")

def maf(): # c'est une fonction qui retourne ce tableau
    t = [allmind(), allcraft(), totalcraft(10)]
    return t


maf() # ceci va afficher les elements des print des fonctions et vas aussi executer les fonctions
print(maf()) # vas afficher [none, none, none] car les elements du tableau sont des fonctions et non des variables ordinaires

# fait exactement la même chose que les deux instruction qui sont juste en haut
t = [allmind(), allcraft(), totalcraft(10)]
t
print(t)



# On peut combiner les decorateurs
@deco_07
@repeter(4)
def prefinal_fonc():
    print("Partie sur les fonctions terminer")

prefinal_fonc() # vas afficher:
             # New trick !!! Avant la fonction final_fonc
             # Partie sur les decorateurs et fonctions terminer
             # Partie sur les decorateurs et fonctions terminer
             # Partie sur les decorateurs et fonctions terminer
             # Partie sur les decorateurs et fonctions terminer
             # New trick !!! Après la fonction final_fonc

@repeter(4)
@deco_07
def final_fonc():
    print("Partie sur les decorateurs terminer")

final_fonc() # vas afficher:

             # New trick !!! Avant la fonction final_fonc
             # Partie sur les decorateurs terminer
             # New trick !!! Après la fonction final_fonc

             # New trick !!! Avant la fonction final_fonc
             # Partie sur les decorateurs terminer
             # New trick !!! Après la fonction final_fonc

             # New trick !!! Avant la fonction final_fonc
             # Partie sur les decorateurs terminer
             # New trick !!! Après la fonction final_fonc

             # New trick !!! Avant la fonction final_fonc
             # Partie sur les decorateurs terminer
             # New trick !!! Après la fonction final_fonc

# Vous avez vu! L'ordre compte! la decoration qui est citer
# en promier sera aussi appliquée aux autres decorations
# On appel ça le << PATTERN DECORATOR >>