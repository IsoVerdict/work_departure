from numpy import *

random.seed(0)
# A = random.randint(0, 100, [10, 5])     si on utilise ça à la fin la matrice standardisé ne vas contenir que des nombre entier 
                                        # (pourquoi ?  je ne sais pas !)
A = random.randn(10, 5)
print(A)
print(A.shape)

# CHOSE A FAIRE
# On vas standardisé chaque colones de la matrice A. Attention, ne pas standardiser toute la matrice mes les colonnes seulement.
# Standardiser, c'est en quelques sort normaliser une chose, il existe  plusieurs sorte de standardisation, nous allons utiliser
# celle qui consiste à faire << chaque éléments d'un certain ensemble moin la moyenne de l'esemble considéré (ici, lorsque l'on
# vas travailler sur une colone cet ensemble sera la colone en question) le tous divisé par l'écart-type de cette ensemble >>
# REMARQUE : si l'on voulais standardiser toute la matrice, l'ensemble considéré serai la matrice

def stand(matrice):
    if matrice.ndim == 1:
        matrice = matrice.reshape((matrice.shape[0], 1))
    for j in range(matrice.shape[1]):
        for i in range(matrice.shape[0]):
            matrice[i, j] = (matrice[i, j] - matrice.mean())/matrice.std()
    return matrice


def stand_by_column(matrice):
    tmp_matrice = stand(matrice[:, 0])

    for i in range(1, matrice.shape[1]):
        tmp_column = stand(matrice[:, i])
        tmp_matrice = concatenate((tmp_matrice, stand(tmp_column)), axis=1)

    
    
    return tmp_matrice


tmp = stand_by_column(A)
print(tmp)
print(tmp.shape)

# ce n'est pas fini !!!!!!!!!!!! 
# car il faut comprendre pourquoi ça ne marche pas avec << A = random.randint(0, 100, [10, 5]) >>





# ---------------------------------------------------------------------------------------------------------------------------------
# SOLUTION de exercice3_stats_maths avec le broadcasting

D = (A - A.mean(axis=0)) / A.std(axis=0) # FIN !!!!!!!!!!!
# EXPLICATIONS:
# ------ la parenthèse : (A - A.mean(axis=0)) ---------
#
#    A       -  A.mean(axis=0)        rappelons que << A.mean(axis=0) >> est un vecteur contenant 
#                                     la moyenne de chaque coione de dimension (5,) c'est à dire 1 ligne 5 colones
#   (10, 5)  - (5,)
# 
#    c'est comme si on fesait 
#
#   (10, 5)  - (1, 5)                 donc le broadcasting dit que étant donnée une coordonnées de << A.mean(axis=0) >> 
#                                     (la i-ième coordonnée) elle sera retiré à la colonne de A corespondante (la i-ième colonne)
#                                     c'est à dire elle sera retiré à chaque éléments de la i-ième colonne de A
#
#
#
#
# ------- la division par A.std(axis=0) ------------
# 
#   (la parenthèse)   /   A.std(axis=0)
#
#   (10, 5)           /   (5,)
# 
#    c'est comme si on fesait 
#
#   (10, 5)           /   (1, 5)      donc le broadcasting dit que étant donnée une coordonnées de << A.std(axis=0) >> 
#                                     (la i-ième coordonnée) elle vas diviser la colonne de A corespondante (la i-ième colonne)
#                                     c'est à dire elle vas diviser chaque éléments de la i-ième colonne de A
#
# Et le tous sera mis dans << D >> une nouvelle matrice, et c'est le résultat voulu !!!!!!!!!