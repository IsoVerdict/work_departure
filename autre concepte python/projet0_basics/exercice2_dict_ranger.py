dico = {
    "positif":[],
    "negatif":[]
}

def trier(dico, nombre):
    if nombre > 0:
        dico["positif"].append(nombre)
    elif nombre < 0:
        dico["negatif"].append(nombre)
    else:
        pass
    return dico