import numpy as np
from scipy import datasets
import matplotlib.pyplot as plt

# on peut aussi faire la même chose qu'avec contour plot, mais en plus precis et lisse
# il suffit juste de passer << Z >> à imshow()
f = lambda x, y: np.sin(x) + np.cos(x+y)*np.cos(x)
X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)

Z = f(X, Y)
plt.imshow(Z)
plt.colorbar()
plt.show()
