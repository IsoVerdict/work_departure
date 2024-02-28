import glob
dico = {}
tmp = ""
filenames = glob.glob("C:/Users/KOKOU/Desktop/CODE_CEDRIC/autre concepte python/projet0_basics/*.txt")
# print(glob.glob("C:/Users/KOKOU/Desktop/CODE_CEDRIC/autre concepte python/projet0_basics/*.txt"))
# print(glob.glob("*.txt"))

for file in filenames:
    with open(file, "r") as f:
        tmp += (" "+f.read())
    dico[file] = tmp
    tmp = ""

print(dico)