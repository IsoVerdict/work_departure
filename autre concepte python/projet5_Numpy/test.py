import numpy

numpy.random.seed(0)
A = numpy.random.randint(0, 10, [5, 5])

tmp = A[:, 1]

print(tmp.shape)
print(tmp.ndim)
print(type(tmp))

print(type(A[:, 1]))


stand_by_column_matrice = numpy.empty((10, 3))
print(stand_by_column_matrice)
print(stand_by_column_matrice.shape)
stand_by_column_matrice[:, 0] = 0
print(stand_by_column_matrice)

numpy.delete(stand_by_column_matrice, 1, 0) # vas suprimer la première colonne de la matrice A
print(stand_by_column_matrice)
print(stand_by_column_matrice.shape)