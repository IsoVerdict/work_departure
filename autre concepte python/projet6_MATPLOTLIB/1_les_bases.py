import numpy as np
# Il y a deux façons de faire des graphiques dans matplotlib, par fonction << plt.plot(x, y) ; plt.show() >>,
# par POO << fig, ax = plt.subplots() ax.plot(x, y) plt.show() >>



# Par Fonction ------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# on vas entrée des données X et Y qu'on veut afficher sur un graphique de cette façons plt.plot(X, Y)

x = np.linspace(-20, 20, 500)   # un tableau de 20 nombres allant de 0 à 2
y = x**2                    # un tableau contenant le carré des éléments du tableau x
##plt.plot(x, y)              # pour tracer le graphique. ATTENTION !!!!! ( X et y doivent avoir la même taille )
##plt.show()                  # pour afficher le graphique

# D'autre parametre
#       plot(x, y, label=[Nom de la courbe] , lw=[Epaisseur du trait], ls=[Style du trait], c=[Couleur du trait])
#
# [Nom de la courbe]        : "choisi le nom que tu veut", "hiveside", "exponential", etc...
# [Epaisseur du trait]      : 5, 10, 2, 23, etc...
# [Style du trait]          : "--" , etc...
# [Couleur du trait]        : "black", "red", "blue", "yellow", etc...

#plt.scatter(x, y)           # pour tracer un nuage de points

# En réalité quand on veut faire une figure dans matplotlib il faut d'abord faire (IL FAUT COMMENCER PAR FAIRE CA,
# dites vous que c'est RECOMMANDE) plt.figure() cela créer une figure toute vide, c'est un peu comme la feuille
# sur laquel on vas travailler. On debute alors le cyle de vie d'une figure , on peut faire plusieur plt.plot(...) à 
# la suite, se qui vas tracer les un apres les autres sur notre figure.
# Ceci prend fin lorsqu'on utilise plt.show()
# Puis l'on peut encore faire plt.figure() puis faire des opérations ... puis faire plt.show()
# Et ainsi de suite, cela vas afficher les fenetre des figure les une apres les autres
plt.figure()
##plt.figure(figsize=(12,8))        # pour changer les dimensions de la figure. Savoir que les distance sur la figure sont 
                                    # en "inch" (c'est à dire en "pouce")
plt.plot(x, y, ls='--', label='quadratique')
plt.plot(x, x**3, c='yellow', label='cubique') 
plt.title("figure 1")                   # un titre à notre figure
plt.xlabel("les abscisses")             # un nom à l'axe x
plt.ylabel("voici les ordonnées")       # un nom à l'axe y
plt.legend()                            # vas afficher les label de tous nos plt.plot(...) sur la figure

plt.show()                              # afficher la figure

plt.savefig("figure1.png")              # pour saugarder la figure sous la forme d'une image png, dans le dossier de
                                        # travaille ici ../../../CODE_CEDRIC


plt.figure()                            
plt.plot(x, np.cos(x), c="grey")
plt.show()

plt.figure()
plt.subplot(2,3,1)                      # Pour créer une grille de grapghique sur notre figure, ici 2 lignes 3 colonnes,
                                        # et le dernier parametre sers à preciser sur quel grille on veut travailler
plt.plot(x, x**3, c='yellow', label='cubique')
plt.title("fig. cubibe")

plt.subplot(2,3,2)
plt.plot(x, np.cos(x), c="grey")
plt.title("fig. cosine")

plt.show()



# Par POO -----------------------------------------------------------------------------------------------
fig, ax = plt.subplots     # On créer une figure << fig >> et un axe << ax >>, ce sont des objets
ax.plot(x, y)              # On obtient le même resultat qu'avec l'autre méthode
plt.show()


fig, ax = plt.subplots(2, 1, sharex=True)    # Pour faire plusieurs graphiques, mais là il faut faire ce qui 
                                            # suis sinon il y aura une érreur

ax[0].plot(x, y)                            # il faut faire ax[0] pour le premier graphique
ax[1].plot(x, np.sin(x))                    # il faut faire ax[1] pour le deuxieme graphique
plt.show()