# Les variables de base

premier_nombre = 13 # int - nombre entier
deuxieme_nombre = 24.34 # float - nombre décimale

premier_texte = 'Hello World' # str - chaine de charactères
deuxieme_texte = "Aujourd'hui" # str

premier_booleen = True # bool - valeur booléenne qui contiens l'une des deux valeurs vrai/faux
deuxieme_boolean = False # bool

# Les opérations

premiere_somme = premier_nombre + deuxieme_nombre + 24
premiere_multiplication = premiere_somme * 2

somme_de_texte = premier_texte + " " + deuxieme_texte
multiplication_de_texte = 3 * premier_texte

premier_et_deuxieme_booleen = premier_booleen and deuxieme_boolean # retourne False
premier_ou_deuxieme_booleen = premier_booleen or deuxieme_boolean # retourne True
not_premier_booleen = not premier_booleen # retourne False

nombre_un_plus_petit_que_deux = premier_nombre < deuxieme_nombre
nombre_un_plus_grand_ou_egale_a_deux = premier_nombre >= deuxieme_nombre
nombre_un_egale_a_deux = premier_nombre == deuxieme_nombre
nombre_un_different_de_nombre_deux = premier_nombre != deuxieme_nombre

premier_texte_different_deuxieme = premier_texte != deuxieme_texte
premier_texte_egale_deuxieme = premier_texte == deuxieme_texte

# Les conversions
nombre_decimale = 12.43
nombre_entier = int(nombre_decimale)
nombre_decimale_2 = float(nombre_entier)

nombre_en_texte = "12"
nombre_entier_2 = int(nombre_en_texte) + 34

nombre_decimale_en_texte = str(nombre_decimale) + " est ton nombre" 

# Lire une valeur entrée par l'utilisateur
valeur_utilisateur_1 = int(input("Entrez un premier nombre: "))
valeur_utilisateur_2 = int(input("Entrez un deuxième nombre: "))
somme_valeurs = valeur_utilisateur_1 + valeur_utilisateur_2

print(str(valeur_utilisateur_1) + " + " + str(valeur_utilisateur_2) + " = " + str(somme_valeurs))