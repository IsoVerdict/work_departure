# pour importer numpy
import numpy

# créer un ndarray

# numpy.array(objet:liste), la c'est un tableau à une dimension, donc une liste [1, 2, 3]
tableau =  numpy.array([1, 2, 3])

# pour voir la dimension du ndarray
tableau.ndim

# renvoie un tuples dont les elements sont la taille de chaque dimension
tableau.shape

# renvoie le nombre d'elements qu'il y a dans notre tableau
tableau.size

# pour créer un tableau de 3 lignes 2 colones remplis de zeros < 0 >
# numpy.zeros(shape)
B = numpy.zeros((3, 2))

# pour créer un tableau de 3 lignes 4 colones remplis de un < 1 >
# numpy.ones(shape)
D = numpy.ones((3, 4))

# pour créer un tableau de 2 lignes 4 colones remplis de neuf < 9 > 
# numpy.full(shape, value)
E = numpy.full((2, 4), 9)

# pour créer un tableau de 3 lignes 4 colones remplis de nombres aléatoires, 
# qui ont été générés à partir de la distribution normal centrée en zéro
# Pour reproduire le même aléatoire on utilise numpy.random.seed(0) , à la place
# de zero < 0 > on peut mettre n'importe quel nombre, l'aléatoire généré dependra 
# du nombre que vous allez mettre mais pour un nombre donné, par exemple ici 
# zero < 0 >, l'aléatoire généré (c'est à dire les nombres aléatoires générés) ne 
# changera pas même si vous relancez le programme, et cet aléatoire differe d'un nombre
# à l'autres, mais est unique pour un même nombre
F = numpy.random.randn(3, 4)

# pour créer une matrice identité de taille 4
G = numpy.eye(4)

#
# numpy.linspace(début, fin, quantité)
H = numpy.linspace(0, 10, 20)

#
# numpy.arange(début, fin, pas)
I = numpy.arange(0, 10, 0.5)

# on peut choisir le type de donnée dans nos ndarray, on plus on peut aussi choisir le 
# nombre de bites que vas occupées nos valeurs dans la mémoire de l'ordinateur, plus le 
# nombres de bites est grand, meilleur sera la précision de notre programme, et notre 
# programme sera plus performant, mais en revanche il sera bien plus lent à l'execution
# Pour ce faire on utilise le parametre dtype, ce paramettre peut s'utiliser sur les 
# methodes qu'on vient de voir 
# numpy.random.randn()
# numpy.linspace()
# numpy.arange()
# numpy.full()
# numpy.ones()
# numpy.zeros()
# numpy.array()
# en en le precisant à la fin.
# ici on créer un tableau qui est en faite une liste, dont les nombre sont des float occupants 16 bits dans la memoire de l'ordinateur
J = numpy.linspace(0, 10, 20, dtype=numpy.float16)

# pour coller la matrice D à la droite de la matrice B et ainsi donné une nouvlle
# matrice, attention les matrices doivent avoir le même nombre de lignes
K = numpy.hstack((B, D))
# K = numpy.concatenate((B, D), axis = 1) donne le même resultat

# pour coller la matrice F en bas de la matrice E et ainsi donné une nouvlle matrice,
# attention les mattrice doivent aavoir le même nobre de colones
L = numpy.vstack((E, F))
# L = numpy.concatenate((E, F), axis = 0) donne le même resultat

# Cette methode permet de redimensionner un tableau
# Attention cette methode ne fonctionne que si le nombre d'éléments 
# qu'on n'a dans le tableau de depart est égale au nombres d'éléments 
# qu'on a dans le tableau d'arriver
C = numpy.arange(0, 11, 0.5) # C contient 12 éléments
C = C.reshape((3, 4)) # effectivement un tableau de 3 lignes et 4 colones contient bien 12 éléments


# Une suptilité ----------------------------
A = numpy.array([1, 2, 3])
A.shape # affiche (3,) , c'est une dimension (ou un état) un peut spéciale pour l'affichage des images
A = A.reshape((A.shape[0], 1)) # pour emmener le tableau A à un état ou il sera concidéré comme une matrice
A.shape # affiche (3, 1) , c'est à présent une matrice et l'on peut faire des calcules matricielles avec!

A = A.squeeze() # pour revenir à l'état un peut spéciale pour l'affichage des images
A.shape # affiche (3,)

A = numpy.random.randn(20, 20)
numpy.delete(A, 1, 0) # vas suprimer la deuxieme ligne de la matrice A
                      # numpy.delete(arr, obj, axe=...)
                      #     arr : tableau d’entrée
                      #     obj : numéro de ligne ou de colonne à supprimer
                      #     axe : Axe à supprimer

numpy.delete(A, 1, 1) # vas suprimer la deuxieme colonne de la matrice A
numpy.delete(A, 0, 1) # vas suprimer la premiere colonne de la matrice A

# On peut spécifiez les numéros de ligne et les numéros de colonne à supprimer dans une liste ou un tableau.
numpy.delete(A, [0, 2, 5], 1) # vas suprimer la 1-ière, 3-ième et 6-ième colonne de la matrice A
numpy.delete(A, [0, 1, 3, 8], 0) # vas suprimer la 1-ière, 2-ième, 4-ième et 9-ième ligne de la matrice A

# Utilisez numpy.s_[] si vous voulez écrire sous la forme [ debut : fin : pas ].
numpy.delete(A, numpy.s_[:2], 1) # vas suprimer de la 1-ière à la 2-ième colonne de la matrice A
numpy.delete(A, numpy.s_[1:5], 0) # vas suprimer de la 2-ième à la 4-ième ligne de la matrice A



# cette methode permet de convertir un tableau à n dimendions en un tableau à une dimension
# c'est comme si on fesait C = C.reshape((C.size, 1))
C = C.ravel()