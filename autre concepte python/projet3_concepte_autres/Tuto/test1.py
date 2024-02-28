

# importation
import test    #pour utilisée la fonction affiche() qui se trouve dans le fichier test.py (module)
test.affiche()

import test as t1 # pour donner en quelque sorte un autre nom à notre module
t1.affiche()

from test import affiche #pour utilisée la fonction affiche() qui se trouve dans le fichier test.py (module)
affiche()                # ici on n'a pas besoin de faire test.affiche

from test import *       #pour importer toutes les fonctions qui se trouve dans le fichier test.py (module)
affiche()                # ici on n'a pas besoin de faire test.affiche

from test import affiche, affiche1  #pour utilisée les fonctions affiche() et affiche1() qui se trouve dans le fichier test.py (module)
affiche()
affiche1()

import pacdoc               # pour importer un package
pacdoc.test3.affiche2()     # pour utiliser la fonction affiche2 qui est dans le fichier(ou module) test3.py qui est dans le package pacdoc
                            # pour créer un package on crée un dossier qui contient un fichier qui à pour nom __init__.py
                            # meme si le fichier ne contient rien il sera consideré que le dossier est un package
                            # un package peut contenir des fichier (qui sont appelé module) et d'autres packages encore


from pacdoc import test3    # pour importer le fichier(ou module) test3.py qui est dans le package pacdoc
test3.affiche2()            # pour utiliser la fonction affiche2 qui est dans le fichier(ou module) test3.py en fesant au préalable "from pacdoc import test3 "


from pacdoc.test3 import affiche2   # pour importer la fonction affiche2 qui est dans le fichier(ou module) test3.py qui est dans le package pacdoc
affiche2()                          # pour utiliser la fonction affiche2 en fesant au préalable "from pacdoc.test3 import affiche2 "