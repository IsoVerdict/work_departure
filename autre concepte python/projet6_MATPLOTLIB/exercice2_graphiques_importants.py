from numpy import *
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target

def graphique(dataset):
    data_width_size = dataset.shape[1]

    plt.figure(figsize=(12, 8))    # Pour faire plusieurs graphiques
    for k in range(0, data_width_size):
        plt.plot(dataset[:,k], label=f"Graphe N°{k}")
        plt.legend()

    plt.show()

graphique(x)