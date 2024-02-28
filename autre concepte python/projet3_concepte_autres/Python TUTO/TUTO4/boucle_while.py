import random


# 1. Choisir un nombre au hazar
juste_prix = random.randint(0, 1000)
estimation = -1
abandon = False

# 2. Tant que l'utilisateur n'as pas trouvé le bon nombre
while estimation != juste_prix:

    # 2.1. Demander un nombre à l'utilisateur
    instruction = input("Quelle est votre estimation? [Q: Quitter] ")
    if not instruction.isnumeric():
        if instruction == 'Q':
            abandon = True
            break
        else: 
            print("Veuillez entrer un nombre ou la lettre Q pour quitter!")
            continue

    estimation = int(instruction)

    # 2.2. Si le nombre est trop petit on va afficher le message "c'est plus"
    if estimation < juste_prix:
        print("c'est plus")

    # 2.3. Si le nombre est trop grand on va afficher le message "c'est moins"
    if estimation > juste_prix:
        print("c'est moins")

# 3. Féliciter l'utilisateur
if abandon:
    print("Dommage le juste prix était: " + str(juste_prix))
else:
    print("Félicitation vous avez bien trouvé le prix: " + str(juste_prix))