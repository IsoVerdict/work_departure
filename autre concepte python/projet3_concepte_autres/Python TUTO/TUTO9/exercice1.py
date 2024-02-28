from bonjour import dire_bonjour, dire_au_revoir
from physique import trajet
from physique.vitesse import convertir_ms_en_kmh

nom = input("Quelle est votre nom? ")
distance = float(input("Quelle distance souhaitez-vous parcourir? "))
vistesse_en_ms = float(input("A quelle vitesse? [m/s] "))

# dire bonjour à l'utilisateur
dire_bonjour(nom)

# convertir vitesse en km/h
vitesse_en_kmh = convertir_ms_en_kmh(vistesse_en_ms)

# calculer temps de trajet
temps_de_trajet = trajet.temps_de_trajet(distance_en_km=distance, vitesse_en_kmh=vitesse_en_kmh)

# afficher temps de trajet
print(f"Votre temps de trajet est de {temps_de_trajet} heures.")

# dire au revoir
dire_au_revoir(nom)