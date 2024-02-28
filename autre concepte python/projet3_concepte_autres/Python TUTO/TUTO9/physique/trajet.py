def temps_de_trajet(distance_en_km, vitesse_en_kmh, nombre_de_pauses = 0, nombre_de_passgers = 0):
    temps = distance_en_km / vitesse_en_kmh
    temps_de_pauses = nombre_de_pauses * 5 / 60
    temps_de_pauses_passagers = nombre_de_pauses * nombre_de_passgers * 2 / 60
    return temps + temps_de_pauses + temps_de_pauses_passagers