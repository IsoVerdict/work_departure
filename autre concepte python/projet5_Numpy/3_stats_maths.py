import numpy

# -----------------------------------------------------------------------------------------------------------------------------------------
# STATISTIQUES ----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
A = numpy.random.randint(0, 10, [2, 3])

A.sum # pour faire la somme de tous les elements de notre tableau
A.sum(axis=0) # renvoie un vecteur (une liste en faite) dont les coordonnées sont la somme des colonnes de la matrice A
A.sum(axis=1) # renvoie un vecteur (une liste en faite) dont les coordonnées sont la somme des lignes de la matrice A

A.cumsum()          # fait la somme cumulée des elements de la matrice
A.cumsum(axis=0)    # renvoie un vecteur (une liste en faite) dont les coordonnées sont la somme cumulée des colonnes de de la matrice A

A.prod(axis=1)      # le produit ... (suivre la même logique que la somme)
A.cumprod()         # produit cumulée ...

A.min()             # minimum...
A.max(axis=1)       # maximum...
A.argmin(axis=0)    # revoie une liste dont les coordonnées sont la position (numero de ligne) du minimum de chaque colonnes de la matrice
A.argmax()          # revoie la position (numero de ligne et de colonne) du maximum

A.sort()            # revoie la même matrice dont les éléments des lignes on été trié par ordre croissant

A.argsort()         # renvoie une matrice telle que, les éléments de la i-ième ligne de cette metrice sont les numeros de colonnes des 
                    # éléments de la "i-ième ligne de la metrice A triés dans l'ordre croissant"


A.mean()        # moyenne ....
A.var(axis=0)   # liste des variances des éléments de chaques colonnes ( pour faire simple on pourra dire "la variance suivant l'axe 0",
                # de même "la moyenne suivant l'axe 0", ou encore "l'écart-type suivant l'axe 0"
A.std()         # écart-type ...

numpy.corrcoef(A) # renvoie  une matrice qui contient les corelation ligne pour ligne (voir video 12 à 10min 20seconds)

numpy.unique(A, return_counts=True) # renvoie deux liste, la première contient les différents éléments de la matrice A et
                                    # le deuxième liste contient le nombre de fois que les éléments de la première liste se
                                    # repete dans la matrice A
# on peut mettre ces deux listes dans des variables
values, counts = numpy.unique(A, return_counts=True)

values[counts.argsort()]            # analysez bien ce code il permet de classer les éléments qui apparaisse le plus souvents 
                                    # au au élément qui apparaisses le moins souvent dans la matrice A (on diras classement
                                    # par ordre d'apparution ou fréquences d'apparution)

# Not a Number, ATTENTION !!!!!!!!!!!!!!!!!!!!
numpy.nan                           # est une entité numpy, qui designe quelque chose qui n'est pas un nombre, cela arrive parfois de
                                    # travailer avec des matrices qui contiennent à certain endroits le fameux "numpy.nan", et si l'on
                                    # fait la moyenne, ou variance, ou ecart-type de telle matrice on trouve "numpy.nan". Donc il faut
                                    # faire attention.

# ce sont des fonctions qui vont calculer la moyenne, variance, ecart-type en ignorant les "numpy.nan", il y en a encore bien d'autres
numpy.nanmean()
numpy.nanvar()
numpy.nanstd()

numpy.isnan(A)          # renvoie un mask indiquant où l'on a un "numpy.nan"

numpy.isnan(A).sum()    # renvoie le nombre de fois que "numpy.nan" se repete dans la matrice A, en effet si True vaut 1 et False vaut 0,
                        # alors cela s'explique.

A[numpy.isnan(A)] = 0   # remplace tous les "numpy.nan" presents dans la matrice A par 0






# ---------------------------------------------------------------------------------------------------------------------------------------------
# ALGEBRE LINEAIRE ----------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------

A = numpy.ones((2, 3))
B = numpy.ones((3, 2))

A.T             # pour trasposer la matrice A

A.dot(B)        # pour le produit matricielle de A et B

numpy.linalg    # est un package numpy pour faire de l'algebre linéaire

from  numpy import linalg

linalg.det(A) # le determinant
linalg.inv(A) # l'inverse

linalg.eig(A) # renvoie deux tableau, le 1-er contient les valeur propres
              # le 2-ième les vecteurs propre (biensur ces vecteurs propres sont aussi des tableaux)
