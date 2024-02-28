import numpy as np
     

# le broadcasting consiste à étendre les dimensions d'un tableau
A = np.ones((2, 3))
B = 3
print(A+3)
print(A+B) # résultat 1, vas additionner chaque éléments de A au scalaire 3
 

A = np.ones((2, 3))
B = np.ones((2, 1)) # B a une colonne, elle sera étendu sur les trois colonnes de A
print(A+B) # résultat 2, vas additionner chaque vecteur colonne de A au vecteur B (en effet B est comme un vecteur là)
 

A = np.ones((2, 3))
B = np.ones((2, 2))
print(A+B) # le broadcasting ne fonctionne pas ici

# en effet, le broadcasting fonctionne lorsque << mis cote à cote les dimenssions des matrice que l'on veut additionner
# doivent être égales ou lorsqu'elles sont différentes (les dimensions d'un même axe) au moins l'une d'elles doit être égal à << 1 >>

A = np.array([5], [0], [3], [3])  # vecteur colonne de dimension (4, 1)
B = np.array([-2, 2, 5])          # vecteur ligne de dimension   (1, 3) << cela fonctionne avec des tableau de dimension de cee genre (3,) >>

print(A+B)                        # ceci vas donné une matrice   (4, 3) et regarder ce qu'elle contient le principe du broadcasting
                                  # est facile à comprendre

# Je viens de dire que << cela fonctionne avec des tableau de dimension de cee genre (3,) >>, en effet ceci est un avertissement pour dire que
# le mieux est d'utiliser la methode numpy.reshape() pour que de telle objets puis avoir de vrai dimension (1, 3) plutôt que (3,). Car si vous
# n'utilisez pas souvent la methode numpy.reshape pour regler le probleme de dimension de telle objets, il peut se produire un broadcasting
# accidentelle et faire des erreurs et bugs dans le programme! Croyez moi, cela peut causer des erreurs. 

# SOLUTION de exercice3_stats_maths avec le broadcasting

D = (A - A.mean(axis=0)) / A.std(axis=0)
