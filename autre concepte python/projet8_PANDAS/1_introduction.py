import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                     # pour importer pandas

data = pd.read_excel("titanic3.xls")    # pour charger un fichier excel qui est en faite un dataset
                                        # pour charger selon le type de donnés read_csv, read_excel, read_.....

data.shape       # renvoie les dimensions de notre dataset
data.head()      # renvoie les premieres lignes de notre dataset
data.columns     # renvoie les colonnes de notre dataset


# pour éliminer certaines colonnes de notre dataset
data = data.drop(['name', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'], axis=1)

data.describe()  # renvoie un tableau contenant les statistique de bases pour chacune de nos colonnes


data = data.dropna(axis=0) # pour élimimer des lignes (les lignes ou il y a des informations manquantes)

# pour les fonctions qui modifient un dataframe (dataset sous forme de tableau en faite), drop(), dropna(), set_index(), replace(), ...
# << inplace >> permet de mettre en place le résultat d'une fonction sur son dataframe 
data = data.dropna(axis=0)
# équivalent:
data.dropna(axis=0, inplace=True)

data.shape


data['age'].hist()                  # pour faire l'histogramme des ages (biensur hist est une fonction matplotlib)
data.groupby(['sex']).mean()        # << groupeby >>, permet de regrouper les gens suivant une categorie, et << mean >> nous permet de faire
                                    # la moyenne (on pouvait utilisé une autre fonction à la place de mean)

data.groupby(['sex', 'pclass']).mean() # on a regrouper selon le sexe de la personne et la classe dans laquelle il était, puis on a fait la moyenne 

data['pclass'].value_counts() # renvoie un tableau qui contient le nombre de passager de chaque classes
data['pclass'].value_counts().plot.bar() # on créer un graphique matplotlib avec ces données


# Dans pandas il y a deux structure de données les << séries >> et les << dataframes >>
# Une << série >>, c'est une colonne dans un << dataframe >>, donc si on assemble plusieurs séries cela donne un dataframe
# En faite une << série >> est un tableau numpy à une dimension auquel on a rajouté une colonne d'index (à ne pas confondre
# avec l'index du tableau numpy)
# on peut choisir d'indexer par des noms plutôt que des nombres
data = data.set_index("name")
data["age"]

# En gros un dataframe est un dictionnaire de séries
#
#                  Rappel:      Dictionnaire["clef"]    =    valeur
#         est semblable à:      DataFrame["column"]     =    une série     


data[data['age'] < 18]['pclass'].value_counts() # on considère les passagés mineurs et l'on conte combien il y en avais par classes

data.iloc[0, 0]                 # pour faire de l'indexing, slicing, etc... comme dans numpy

data.loc[0:2, "age"]            # pour faire sur une colonne de l'indexing, slicing, etc... comme dans numpy
data.loc[0:2, ["age", "sex"]]   # pour le faire sur deux colonnes, voir plusieurs