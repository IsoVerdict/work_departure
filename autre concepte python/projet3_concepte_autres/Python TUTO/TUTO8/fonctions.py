print("Avant la définition")

def dire_bonjour():

    print("Hello World")
    print("Bonjour")

print("Après la définition")
dire_bonjour()
dire_bonjour()
dire_bonjour()

def temps_de_trajet(distance_en_km, vitesse_en_km_h, nombre_de_pauses = 0, nombre_de_passgers = 0): # à partir du moment où l'on definit une valeur par defaut pour un parametre defonction, 
                                                                                                    # tous les parametres qui suive celui ci doivent aussi posseder une valeur par defaut
    temps = distance_en_km / vitesse_en_km_h
    temps_de_pauses = nombre_de_pauses * 5 / 60
    temps_de_pauses_passagers = nombre_de_pauses * nombre_de_passgers * 2 / 60
    return temps + temps_de_pauses + temps_de_pauses_passagers

temps_1 = temps_de_trajet(120, 30, 1)
temps_2 = temps_de_trajet(40, 40, 2, 5)

temps_total = temps_1 + temps_2

print(f"Le temps total est égale à {temps_1} h + {temps_2} h = {temps_total} h")

temps_3 = temps_de_trajet(nombre_de_passgers=2, distance_en_km=23, vitesse_en_km_h=1)
print(f"Le temps necessaire = {temps_3} h")

temps_4 = temps_de_trajet(40, 20, nombre_de_passgers=2) # à partir du moment ou l'on mentionne le nom d'un paramettre à l'appel 
                                                        # d'une fonction, tout les paramettres qu'on mettra à la suite devront 
                                                        # aussi être mentionné
print(temps_4)