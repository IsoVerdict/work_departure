import numpy

A = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # ceci est une matrice de 3 lignes 2 colones, donc la dimension du ndarray est 2

# l'indexing
A[1, 0] # pour acceder à l'élément de la ligne 0 et de la colone 1, donc vas afficher << 4 >>

# slicing
A[:, 0] # vas renvoyer (c'est à dire qu'on aura accés) une liste qui contient tout les éléments qui sont sur la colone 0
A[1, :] # vas renvoyer (c'est à dire qu'on aura accés) une liste qui contient tout les éléments qui sont sur la ligne 1
A[1] # ceci est un racourci pour la commande précedante, vas renvoyer une liste qui contient tout les éléments qui sont sur la ligne 1

A[0:2, 0:2] # vas selectionner (c'est à dire qu'on aura accés) les éléments des deux premiéres lignes et deux premiéres colones, et ensuite former une nouvelle matrice avec
A[0:2, 0:2] = 10 # les éléments des deux premiéres lignes et deux premiéres colones, auront tous pour valeurs << 10 >>

A[:, -2:] # vas selectionner (c'est à dire qu'on aura accés) les éléments des deux dernières colones, et ensuite former une nouvelle matrice avec
A[:, 1:] # ceci fait la même chose que la commande précedante


B = numpy.zeros((4,4)) # une matrice nulle de taille 4x4
B[1:3, 1:3] = 1 # vas remplacer les quatres zeros du milieu de la matrice par << 1 >>

C = numpy.zeros((5,5))  # une matrice nulle de taille 5x5
                        # C[ début:fin:pas , début:fin:pas ]

C[::2, ::2] = 1         ## les éléments de toutes les lignes en sautant les éléments d'une ligne
                        ## donné d'un pas de << 2 >> et éléments de toutes les colones en sautant 
                        ## les colones (c'est à dire que les éléments de la colone sauté ne seront
                        ## plus concernés) d'un pas de << 2 >>, auront tous pour valeurs << 1 >>

# Boolean indexing
A = numpy.random.randint(0, 10, [5, 5]) # vas créer une matrice 5x5 remplie de valeur pris aléatoirement entre 0 et 9

A < 5                                   # vas renvoyer une matrice 5x5 contenant des booleans dont l'élément de la i-ième
                                        # ligne et j-ième colone sera << True >> si l'élément de la i-ième ligne et j-ième
                                        # colone de la matrice A était strictement inférieur à 5, sinon cet élément sera << False >>
                                        # On appelle une telle matrice (ou tableau) un "mask"

A[A < 5] = 10   # on peut se servir d'un "mask" pour indexer une matrice (ou tableau) de même taille que le "mask", 
                # ici l'élément de la i-ième ligne et j-ième colone de la matrice A sera égale à 10 si l'élément de
                # la i-ième ligne et j-ième colone du mask vaut True, sinon l'élément concidéré (i-ième ligne et j-ième colone)
                # de la matrice A concidéré gardera sa valeur. Cest ça qu'on appel le << Boolean indexing >>

A[(A < 5) & (A > 2)] = 10   # On peut tester plusieurs conditions, ceci aura pour effet d'appliquer les deux conditions (qu'on
                            # peut facilement comprendre) aux éléments de la matrice

A[A < 5] # vas revoyer une liste contenant les éléments de la matrice A strictement inférieur à 5

B = numpy.random.randn(5, 5) # génerer un tableau de 5 lignes 5 colones remplis de nombres aléatoires, qui ont été générés 
                             # à partir de la distribution normal centrée en zéro

B[A < 5] # vas revoyer une liste contenant les éléments de la matrice B qui sont aux endroits où l'on aurai trouver << True >>
         # si l'on etait dans le "mask" au même endroit 