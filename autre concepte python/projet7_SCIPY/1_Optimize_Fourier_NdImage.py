import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d      # pour interpoler
from scipy import optimize                  # pour optimiser
from scipy import signal
from scipy import fftpack                   # pour les transformés de fourier

# ---------------------------------------------------------------------------------------
# Interpolation et minimisation ---------------------------------------------------------
# ---------------------------------------------------------------------------------------

# interpolate ---------------------------------------------------------------------------
x = np.linspace(0, 10, 10)
y = x**2
plt.scatter(x, y) # ceci vas placer quelques point de la fonction x au carré (c'est vrai
                  # qu'ici on connait la fonction mais l'idée c'est d'interpoler un
                  # ensemble de point dont on ne connait pas le lien qui les unis)

f = interp1d(x, y, kind="linear") # pour interpoler on utilise la fonction (methode !!!) << interp1d >> du package << matplotlib.pyplot >>
                                  # cette fonction vas nous permettre de générer une autre fonction f qui est notre fonction d'interpolation
                                  # kind= est le parametre qui désigne le type d'interpolation:  "linear", "nearest", "zero", "slinear",
                                  # "quadratic", "cubic", "previous", "next".

new_x= np.linspace(0, 10, 30)            # on créer en quelque sorte un decoupage ou subdivision de l'intervalle [0, 10]
result = f(new_x)                        # donc result est le nouveau << y >> qui vas contenir les nouveaux points de la fonction d'interpolation

plt.scatter(new_x, result, c="r")        # affiche le resultat, c="r" c'est pour mettre le graphe en rouge




# optimize ---------------------------------------------------------------------------
x = np.linspace(0, 2, 100)
y = 1/3*x**3 - 3/5 * x**2 + 2 + np.random.randn(x.shape[0])/20 # ceci est un polynome du degré 3 au quel on n'a rajouter un peu de bruit
                                                                      # (c'est à dire qu'on a rajouter du desordre)
plt.scatter(x, y)

# optimiser c'est trouver un modele (une fonction) qui colle bien avec le nuage de points, pour ça on vas utiliser la fonction
# (methode !!!) << curve_fit >> du package << optimize >> qui utilise la methode des moindres carrés pour trouver les bon parametres
# (a, b, c, d) de notre modele f qu'on aura créer comme etant une fonction python.
def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

params, param_cov = optimize.curve_fit(f, x, y)     # on donne le modele << f >> et les données qu'il y a dans notre dataset << x >> et << y >>
                                # cette fonction renvoie, deux tableaux, le premier contient les parametre optimisés de notre modele
                                # << f >> en fonction de notre dataset, et le deuxieme tableau contient la matrice de covariance des
                                # parametres de ce model. Nous avons respectivement mis ces deux tableaux dans << params >> et << param_cov >>.

plt.plot(x, f(x, params[0], params[1], params[2], params[3], c="g", lw=3)) # pour afficher le modele optimisé




# minimize ---------------------------------------------------------------------------
def f(x):
    return x**2 + 15*np.sin(x)

x = np.linspace(-10, 10, 100)
plt.plot(x, f(x))

x0 = -5
result = optimize.minimize(f, x0=x0).x # à partir du point x0, la methode << minimize >> vas executer un algorithme de
                                       # minimisation qui vas peu à peu converger vers le premier minimum qu'il rencontrera 
                                       # cette methode renvoie beaucoup d'information mais la coordonné du minimum s'obtien
                                       # en fesant << optimize.minimize(f, x0=-8).x >>
plt.scatter(result, f(result), s=100, c="r", zorder=-1)     # on affiche le minimum trouver par la methode minimize
plt.scatter(x0, f(x0), s=200, marker="+", c="g", zorder=1)  # on affiche le point à partir du quel on effectuer la minimisation


# remarquons qu'on peut minimiser des fonction qui se represente sur des espaces de dimension   n >= 2
# prenons cette fonction fonction que nous avons deja vue
def f (x):
    return np.sin(x[0]) + np.cos(x[0]+x[1])*np.cos(x[0])

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)

x, y = np.meshgrid(x, y)
plt.contour(x, y, f(np.array([x, y])), 20) # pour afficher la fonction

x0 = np.zeros((2, 1))   # comme c'est une fonction qui se represente sur un espace de dimension 3, l'on choisi le point de depart
                        # qui est un point du plan donc ayant deux coordonnées

x0 = x0.squeeze()       # pour que la dimmension de x0 soit de cette forme << (2,) >> sinon ça ne vas pas marcher, car la methode 
                        # << minimize >> vas generer une erreur car c'est un tableau de ce genre de dimension qui doit être donné
                        # à sont parametre << x0= >>

result = optimize.minimize(f, x0=x0).x
plt.scatter(x0[0], x0[1], s=100, marker="+", c="r")         # on affiche le point à partir du quel on effectuer la minimisation
plt.scatter(result[0], result[1], s=100, c="g")     # on affiche le minimum trouver par la methode minimize






# ---------------------------------------------------------------------------------------
# Traaitement du signale ----------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# fonction permettant d'éliminer toute tendance linéaire d'un signale, cette fonction est
# << detrend >>, il faut faire l'importation << from scipy import signal >>
x = np.linspace(0, 20, 100)
y = x + 4*np.sin(x) + np.random.randn(x.shape[0])    # ceci peut être vue comme un signal

plt.plot(x, y)                                       # nous représentons ce signal

new_y = signal.detrend(y)

plt.plot(x, new_y) # on trace notre signale sans la tendance linéaire


# la transformation de fourier est une technique mathématiques qui permet d'extraire et 
# d'analiser les frequences qui sont présentes dans un signale périodique.
# le résultat donne un graphique que l'on appel << spèctre >>, dans lequel en abscisse,
# on observe les fréquences et en ordonné on observe les enplitudes pour chaque fréquences
# pour faire ça avec scipy on importe << fftpack >> et on utilise les méthodes << fft() >>
# et << fftfreq() >>

# Voici un signal
x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x)
plt.plot(x, y)


# transformé de fourier
fourier = fftpack.fft(y)
frequences = fftpack.fftfreq(y.size)

# pour ne pas avoir des fréquences et amplitudes négatives
power = np.abs(fourier)                  # on prend plutôt la valeur absolue des amplitudes
abs_frequences = np.abs(frequences)      # on prend plutôt la valeur absolue des fréquences


plt.plot(abs_frequences, power)          # pour tracer le << spèctre >>


# on peut utiliser la trasformé de fourier pour filtrer un signal
# ETAPE 1: On applique la transformé de fourier à un signal bruillant
# ETAPE 2: Puis l'on remplace certaine valeurs du spètre obtenue en fesant du boolean indexing
# ETAPE 3: Puis l'on utilise la transformer de fourier inverse sur le spèctre nouvellement obtenue afin d'obtenir un signal sans bruit

x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x) + np.random.random(x.shape[0])*10
plt.plot(x, y)

# ETAPE 1: transformé de fourier
fourier = fftpack.fft(y)
frequences = fftpack.fftfreq(y.size)
power = np.abs(fourier)
abs_frequences = np.abs(frequences)


# ETAPE 2: On filtre le signal
fourier[power<400] = 0  # toutes les valeurs du spètre dont l'amplitute est inférieur à 400 aurons à présent zéro pour valeur

# ETAPE 3: transformé de fourier inverse
filtered_signal = fftpack.ifft(fourier) # la methode << ifft() >> permet de faire la transformé de fourier inverse

plt.plot(x, y, lw=0.5) # on trace le signal bruillant
plt.plot(x, filtered_signal, lw=3) # on trace le signal filtrer




# ---------------------------------------------------------------------------------------
# Image processing ----------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# scipy.ndimage propose de nombreuses actions pour le traitement d'images: convolutions,
# filtres de Gauss, méthode de mesures, et morphologie.
# La morphologie est une technique qui permet de transformer une matrice (et donc une image)
# par le déplacement d'une structure sur chaque pixel de l'image. Lorsqu'un pixel "blanc"
# est visité, la structure peut effectuer une opération:
#
#       de dilation: imprime des pixels
#       d'érosion : efface des pixels
#
# Cette technique peut-etre utile pour nettoyer une image des artefacts qui peuvent la composer.

from scipy import ndimage

# Création d'une image avec quelques artefacts
np.random.seed(0)
X = np.zeros((32, 32))
X[10:-10, 10:-10] = 1
X[np.random.randint(0,32,30),np.random.randint(0,32,30)] = 1 #ajout d'artefacts aléatoires
plt.imshow(X)

# opération de binary_opening = érosion puis dilation
open_X = ndimage.binary_opening(X)
plt.imshow(open_X)

# Application : Image processing (cas réel) ---------------------------------------------
# importer l'image avec pyplot
image = plt.imread('bacteria.png')
image = image[:,:,0] # réduire l'image en 2D
plt.imshow(image, cmap='gray') # afficher l'image
image.shape

# copy de l'image, puis création d'un histogramme
image_2 = np.copy(image)
plt.hist(image_2.ravel(), bins=255)
plt.show()

# boolean indexing: création d'une image binaire
image= image<0.6
plt.imshow(image)

# morphologie utilisée pour enlever les artefacts
open_image = ndimage.binary_opening(image)
plt.imshow(open_image)

# Segmentation de l'image: label_image contient les différents labels et n_labels est le nombre de labels
label_image, n_labels = ndimage.label(open_image)
print(f'il y a {n_labels} groupes') # il y a 53 groupes

# Visualisation de l'image étiquetée
plt.imshow(label_image)

# Mesure de la taille de chaque groupes de label_images (fait la somme des pixels)
sizes = ndimage.sum(open_image, label_image, range(n_labels))

# Visualisation des résultats
plt.scatter(range(n_labels), sizes)
plt.xlabel('bactérie ID')
plt.ylabel('taille relative')
plt.show()