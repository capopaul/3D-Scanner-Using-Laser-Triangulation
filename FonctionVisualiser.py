import os
import sys
import subprocess
from FonctionsAnnexes import ecrire
from fonctionsFichier import getBlender

#Fonction qui lance blender
def visualiser():
    lien = getBlender()
    if(lien == "ERROR01"):
        ecrire("Lien vers blender introuvable",color="error")
    else:
        lien = lien.replace("/","//")
        ecrire(lien)
        try:
            subprocess.call([lien,'-P','BlenderScript.py'])
        except FileNotFoundError:
            ecrire("Lien vers blender incorrect",color="error")
