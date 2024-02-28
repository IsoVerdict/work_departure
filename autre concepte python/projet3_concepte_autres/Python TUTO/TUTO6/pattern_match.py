couleur = "toute autre chose"

match couleur:
    case "rouge" | "vert":
        print("Très bon choix de couleur")
    case "bleu":
        print("Belle couleur")
    case _:
        print("je ne suis pas fan de ", couleur)

personne = {
    "age": 15,
    "passion": "timbres"
}

match personne:
    case {"age": age, "passion": "jeux vidéo"} if age >= 18:
        print("Bienvenu vous pouvez jouer autant que vous le voulez")
    case {"age": age} if age < 18:
        print(f"Désolé mais ce salon est réservé aux adultes et vous n'avez que {age} ans")
    case _:
        print("Ce salon est dédié aux adultes passionés de jeux vidéos")