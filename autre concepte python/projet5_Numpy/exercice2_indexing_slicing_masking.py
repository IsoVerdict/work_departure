# from scipy import misc      # obsolet dans SciPy v1.10.0 et vas disparaitre dans SciPy v1.12.0, il faut utiliser scipy.datasets.face
from scipy import datasets
import matplotlib.pyplot as plt

# EN NOIRE ET BLANC
face = datasets.face(gray=True)
plt.imshow(face, cmap=plt.cm.gray)

# EN COULEUR
#face = datasets.face()
#plt.imshow(face)


# zoomer de un quart vers le centre de la photo ------------------------------------------
quart_height = round(face.shape[0]/4)
start_quart_height = 0 + quart_height
end_quart_height = face.shape[0] - quart_height

quart_width = round(face.shape[1]/4)
start_quart_width = 0 + quart_width
end_quart_width = face.shape[1] - quart_width

face_zoom = face[start_quart_height:end_quart_height, start_quart_width:end_quart_width]
# ----------------------------------------------------------------------------------------




# augmenter et diminuer la luminosité ----------------------------------------------------
max_threshold = 210     # seuil maximum
min_threshold = 50      # seuil minimum

face[face > max_threshold] = 255        # si un pixel est au dessus de la valeur de
                                        # max_threshold alors sa valeur vaudra 255, sinon
                                        # il garde sa valeur

face[face < min_threshold] = 0          # si un pixel est en dessous de la valeur de
                                        # min_threshold alors sa valeur vaudra 0, sinon
                                        # il garde sa valeur
# ----------------------------------------------------------------------------------------

plt.imshow(face_zoom, cmap=plt.cm.gray)



print(face)
print(type(face))
print(face.shape)

plt.show()

# CHOSE A SAVOIR
# la photo misc présent dans scipy par défaut a été mise dans l'objet face
# face est un tableau numpy, c'est à dire un ndarray, vous pouvez vérifier avec type(face)
# et on affiche cette photo contenu maintenant dans "face" grace à "matplotlib" via les methodes "imshow()" et "show()"

# CHOSES A FAIRE
# zoomer de un quart vers le centre de la photo
# augmenter la luminausité de certains pixels qui sont dejà au dessus
# d'une certaine luminausité, et aussi reduire la luminausité de 
# certain pixel qui sont deja très sombre

# FINI !!!!!!!!!!!!!!!