recette = {                                                         # pour créer un dictionnaire
    "clé": "valeur",                                                # on met une "clé" suivie de deux point : et d'une "valeur"
    "nom": "Tarte aux pommes",                                      # chose à savoir, on ne peut pas avoir deux fois la même clé dans un dictionnaire
    "temps": 30,                                                    # lorsqu'une clé ou valeur est un nombre on ne mets pas de griffe ""
    "ingredients": ["pommes", "..."],
    "etapes": {
        "preparation": ["couper des pommes", "..."],
        "cuisson": ["cuire au four à 200° pendant 30min", "..."]
              }
} 

recette.values() # revoie un tableau contenant les valeurs du dictionnaires recette
recette.keys() # revoie un tableau contenant les clés du dictionnaires recette
len(recette) # pour connaitre la taille

recette["nom"] = "Autre chose" # pour ajouter la clé "nom" et sa valeur "Autre chose" dans notre dictionnaire
recette["niveau"] = "débutant" # ajoute "niveau" : "débutant"

recette.get("ici")      # renvoie la valeur associé à la clé "ici" ou renvoie << none >> si la clé "ici" n'existe pas 
recette.get("ici", 1)   # renvoie 1 si la clé "ici" n'existe pas, à la place de 1 on pouvais mettre n'importe quoi d'autre

recette.fromkeys(une_liste) # vas ajouter tout les elements de la liste en tant que clés et la valeur associée à chacune de
                            # ces clées est << none >>
recette.fromkeys(une_liste, "une valeur par default") # là la valeur associée à chacune de ces clées est "une valeur par default"

recette.pop("nom") # vas suprimer la clée "nom" et sa valeur associée, et renvoie aussi la valeur associée à cet clée
niveau = recette.pop("niveau")
print(niveau)
print(recette)


recette.update({
    "nom": "Tarte au chocolat",
    "type": "dessert"
})

del recette["temps"]


for cle in recette: # parcour les clées de recette
    print(cle)

for valeur in recette.values(): # parcour les valeurs de recette
    print(valeur)

for cle, valeur in recette.items(): # pour afficher les clées et les valeurs
    print(f"La clé est {cle} et la valeur est {valeur}")


recette["origine"] = "France"
print(recette.get("origine", "Italie"))