import os

"""
Mais à quoi sert ce truc c'est ça ?

xD

Euh en fait les programmes que nous executons dans blender ne peuvent pas lire
de variables car c'est comme si le fichier était copier coller et que donc lorsque
le programme blender l'execute il n'est pas actualisé par le logiciel (donc les
variables non plus).

Pour contrer ça le logiciel ecrit dans un fichier temporaire qui lors de sa fermeture est detruit.
Celà permet au logiciel de blender de venir lire ce fichier et ainsi de contourner le probleme des
variables non actualisé
"""

#       LE FICHIER TEMPORAIRE NE CONTIENT QUE UNE SEULE LIGNE

#pour éditer le fichier temporaire
def edit(link):
    fichier = open("FichierTemporaire.txt", "w")
    fichier.write(link)
    fichier.close()

#Fonction executé lorsque la fenetre du logiciel est fermé"
def delete():
    os.remove("FichierTemporaire.txt")

#classe executé seulement par le programme blender pour récupérer la variable self.lien
class link():
    def __init__(self):
        try:
            fichier = open("FichierTemporaire.txt", "r")
            lien= fichier.readline()
            fichier.close()
            self.lien = lien
        except FileNotFoundError:
            print("Sorry Bro fichier non trouve")
