liste_vide = []
liste_elements_meme_type = [1, 5, 3, 10, 23, 27]
liste_heterogene = [18, 34, 22.22, "Bonjour", "ca va", [3, 2, 1], 120]

# Les opérations
liste_heterogene[2] = 33.33
liste_heterogene.append(200)
liste_heterogene.insert(2, 453)

print(liste_heterogene)

del liste_heterogene[1]
# si l'on tape directement << del list_heterogene >> cela vas tout simplement suprimer la liste au complet

element_efface = liste_heterogene.pop(1)

print(element_efface)
print(liste_heterogene)
print(liste_heterogene[-1])
print(len(liste_heterogene))

somme_de_listes = liste_heterogene + liste_elements_meme_type
print(somme_de_listes)

somme_de_listes.extend(["a", "b"])
print(somme_de_listes)

print(somme_de_listes[1:4])
print(somme_de_listes[5:])
print(somme_de_listes[:6])
