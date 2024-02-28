age = 18
aime_les_jeux_videos = False

if age >= 18:
    print("Vous êtes majeur")
    print("Vous pouvez entrer")

    if aime_les_jeux_videos:
        print("Nous avons une PS5 au bout de la pièce...")
    
    print("La porte est ouverte")

elif age > 0 and age < 18:
    print("Vous êtes mineur")

elif age == 0:
    print("Bienvenu sur terre")

else: 
    print("hmm quel âge étrange...")

print("A bientôt")