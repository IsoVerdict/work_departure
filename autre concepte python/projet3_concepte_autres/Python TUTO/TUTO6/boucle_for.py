liste_entiers = [5, 8, 71, 34, 21]

for entier in liste_entiers:
    print(entier)

print("============")

for nombre in range(2, 10, 3):
    print(nombre)

print("============")

for nombre in range(30, 10, -5):
    print(nombre)

print("===========")

for rep, entier in enumerate(liste_entiers, 2):
    print(f"L'entier {entier} est l'élément n°{rep} de la liste")
