from numpy import *
import matplotlib.pyplot as plt

dataset = { f"experience{i}": random.randn(100) for i in range(4)}

x = linspace(-20, 20, 100)

def graphique_POO(dataset):
    data_size = len(dataset)

    fig, ax = plt.subplots(data_size, 1, sharex=True)    # Pour faire plusieurs graphiques
    for i in range(data_size):
        ax[i].plot(x, dataset[f"experience{i}"], label="experience "+str(i))

    plt.show()

def graphique_plot(dataset):
    data_size = len(dataset)

    plt.figure(figsize=(12, 8))    # Pour faire plusieurs graphiques
    for k, i in zip(dataset.keys(), range(1, data_size+1)):
        plt.subplot(data_size, 1, i)
        plt.plot(dataset[k])
        plt.title(k)

    plt.show()

graphique_plot(dataset)

# ça fonctionne mais le label ne s'affiche pas dans graphique_POO !!!