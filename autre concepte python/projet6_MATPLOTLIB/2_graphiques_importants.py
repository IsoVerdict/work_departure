import numpy as np
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Ceci est une liste des graphiques importants

# 1  plt.scatter()   ---------------------------------------------------

# on charge le dataset .............................................
iris = load_iris()
x = iris.data
y = iris.target

print(f'x contient {x.shape[0]} exmples et {x.shape[1]} variables')
print(f'il y a {np.unique(y).size} classes')
# ...................................................................




# pour representer deux variable sur notre graphique .................
plt.scatter(x[:, 0], x[:, 1], c=y, alpha=0.5, s=x[:,2]*70)  # alpha= c'est pour controler la transparence des points de notre graphe
                                                            # s=x[:,2]*70 c'est pour controler la taille des points de notre graphe
                                                            # en fonction de la nature des fleures(fonction de la longueur du petal)
plt.xlabel('longueur sépal')
plt.ylabel('largeur sépal')



# x contient 150 exmples et 4 variables, il y a 3 classes.......................
n = x.shape[1]
plt.figure(figsize=(12, 8))
for i in range(n):
    plt.subplot(n//2, n//2, i+1)
    plt.scatter(x[:, 0], x[:, i], c=y)
    plt.xlabel('0')
    plt.ylabel(i)
    plt.colorbar(ticks=list(np.unique(y)))
plt.show()


# Graphiques 3D................................................................................
# il faut importer ça << from mpl_toolkits.mplot3d import Axes3D >>
ax = plt.axes(projection="3d")
ax.scatter(x[:, 0], x[:, 1], x[:,2], c=y) # ne pas oublier de charger le dataset dans les variable x et y

plt.show()


# Visualiser des surfaces ou des foction mathématiques en 3D ..................................
# création d'une fonction mathématiques (fonction lambda)
f = lambda x, y: np.sin(x) + np.cos(x+y)

# Maintenant si l'on veut observer f(x,y) en fonction de x et y dans un graphique 3D, on doit créer
# deux vecteurs numpy X et Y allant par exemple de 0 à 5, et créer une grille avec numpy.meshgrid()
# à partir des deux axes X et Y.
X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)
ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z, cmap="plasma") # pour afficher notre graphique 3D
# ne pas oublier de faire plt.show()
plt.show()


# L'Histogramme ..............................................

plt.hist(x[:,0], bins=20) # vas afficher la distribution (histogramme) que suis la variable 0
                          # bins=20 permet de de definir le nombre de subdivisions dehistogramme
plt.hist(x[:,1], bins=20) # vas afficher la distribution (histogramme) que suis la variable 1 à 
                          # la suite de celui de la variable 0

plt.hist2d(x[:,0], x[:,1]) # vas afficher un histogramme en 2D, qui est la visualisation de la 
                           # distribution des données lorsqu'elles suivent deux variables
                           # plt.hist2d(x[:,0], x[:,1], cmap="Blues") pour changer de couleur par exemple
plt.xlabel('longueur sépal')
plt.ylabel('largeur sépal')
plt.colorbar() # vas afficher une bar qui vas nous donnée à quoi correspond les couleurs de notre
               # histogramme (en generale ce sont les fréquances d'apparution)
plt.show()

# bonus sur les histogrammes, utilisation sur les images
# from scipy import misc      # obsolet dans SciPy v1.10.0 et vas disparaitre dans SciPy v1.12.0, il faut utiliser scipy.datasets.face
from scipy import datasets
import matplotlib.pyplot as plt
# EN NOIRE ET BLANC
face = datasets.face(gray=True)
# plt.imshow(face, cmap=plt.cm.gray)  # il ne faut pas utilisez ça ici

# Nous allons faire l'histogramme de cette image de << raton laveur en noir et blanc >>, etant donnée qu'un pixel en noire 
# et blanc prend une valeur compris entre 0 et 255, la subdivision de l'histogramme sera de 255 (bins=255), il serai inutile
# de depasser ce nombre
plt.hist(face.ravel(), bins=255) # remarquons que plt.hist( << une liste >> , bins=255), prend une liste or << face >> est un << tableau >>,
                                 # c'est a dire un << ndarray >> de dimension 2, et l'on a vue que la methode << ravel() >> permet de revoyer
                                 # une liste qui contient tout les elements du tableau sur lequel on utilise la methode (c'est en quelque 
                                 # sorte applatir le tableau)
plt.show()


# LES GRAPHIQUES CONTOURS PLOT ..............................................................................................
# création d'une fonction mathématiques (fonction lambda)
f = lambda x, y: np.sin(x) + np.cos(x+y)
X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)
plt.contour(X, Y, Z, 20, colors="black") # contour(X, Y, Z, << la precision >>, colors="black") , c'est genre de graphique nous permette
                                         # de voir la surface f(x,y) vue de haut comme le relief de montagnes. Remarque lorsqu'on choisi
                                         # la couleur noire les pointillés désigne les valeurs négatifs.

plt.contourf(X, Y, Z, 20, cmap="RdGy") # permet d'avoir le même resultat un peut plus jolie
plt.colorbar() # une legende



# IMAGE SHOW ..................................................................................................................
# premièrement imshow() permet d'afficher des images, mais surtout peut aussi afficher n'importe quel tableau numpy

# par exemple nous allons tracer la matrice de correlation pour notre dataset des fleurs d'iris
# on charge le dataset .............................................
iris = load_iris()
x = iris.data
y = iris.target

plt.imshow(np.corrcoef(x.T), cmap="Blues")  # << x.T >> c'est la transposée de x, corrcoef() est une fonction qui a deja été vue
plt.colorbar()
plt.show()

# on peut aussi faire la même chose qu'avec contour plot, mais en plus precis et lisse
# il suffit juste de passer << Z >> à imshow()
f = lambda x, y: np.sin(x) + np.cos(x+y)
X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)
plt.imshow(Z)
plt.colorbar()
plt.show()
