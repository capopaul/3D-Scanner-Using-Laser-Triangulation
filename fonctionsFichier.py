#from tkinter import *

def getIntCamera():
    try:
        fichier = open("SAVES\config.txt", "r")
        ligne = fichier.readline()
        ligne = fichier.readline()
        valeur = ligne
        if(valeur.find("camera:") == -1):
            return -1
        else:
            valeur = valeur.replace("camera: ", "")
            return int(valeur)
        fichier.close()
    except FileNotFoundError:
        print("Fichier config non trouvé")
def getVersion():
    try:
        fichier = open("SAVES\config.txt", "r")
        ligne = fichier.readline()
        valeur = ligne
        if(valeur.find("version:") == -1):
            return -1
        else:
            valeur = valeur.replace("version: ", "")
            return valeur
        fichier.close()
    except FileNotFoundError:
        print("Fichier config non trouvé")
    
def getUSB():
    try:
        fichier = open("SAVES\config.txt", "r")
        ligne = fichier.readline()
        ligne = fichier.readline()
        ligne = fichier.readline()
        valeur = ligne
        if(valeur.find("usb:") == -1):
            return "ERROR01"
        else:
            valeur = valeur.replace("usb: ", "")
            return valeur.replace("\n","")
        fichier.close()
    except FileNotFoundError:
        print("Fichier config non trouvé")

def getBlender():
    try:
        fichier = open("SAVES\config.txt", "r")
        ligne = fichier.readline()
        ligne = fichier.readline()
        ligne = fichier.readline()
        ligne = fichier.readline()
        valeur = ligne
        if(valeur.find("blender:") == -1):
            return "ERROR01"
        else:
            valeur = valeur.replace("blender: ", "")
            return valeur
        fichier.close()
    except FileNotFoundError:
        print("Fichier config non trouvé")
    
def getNom(fichier):
    ligneNom = fichier.readline()
    nom = ligneNom
    if(nom.find("nom:") == -1):
        return "ERROR01"
    else:
        nom = nom.replace("nom: ", "")
        return nom

def getDate(fichier):
    ligneDate = fichier.readline()
    date = ligneDate
    if(date.find("date:") == -1):
        return "ERROR01"
    else:
        date = date.replace("date: ", "")
        return date
def getPrecision(fichier):
    lignePrecision = fichier.readline()
    Precision = lignePrecision
    if(Precision.find("precision:") == -1):
        return "ERROR01"
    else:
        Precision = Precision.replace("precision: ", "")
        return Precision    
def getDistance(fichier):
    lignePrecision = fichier.readline()
    Precision = lignePrecision
    if(Precision.find("distance:") == -1):
        return "ERROR01"
    else:
        Precision = Precision.replace("distance: ", "")
        return Precision

def getAngle(fichier):
    ligneAngle = fichier.readline()
    angle = ligneAngle
    if(angle.find("angle:") == -1):
        return "ERROR01"
    else:
        angle = angle.replace("angle: ", "")
        return angle
    
def getNbTours(fichier):
    ligneNbTours = fichier.readline()
    nbTours = ligneNbTours
    if(nbTours.find("nbTours:") == -1):
        return "ERROR01"
    else:
        nbTours = nbTours.replace("nbTours: ", "")
        return nbTours

def getHauteurTour(fichier):
    ligneHauteur = fichier.readline()
    H = ligneHauteur
    if(ligneHauteur.find("H:") == -1):
        return "ERROR01"
    else:
        H = nbTours.replace("H: ", "")
        return H

def getHmoins(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Hmoins:") == -1):
        return -1
    else:
        nb = nb.replace("Hmoins: ", "")
        return nb

def getHplus(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Hplus:") == -1):
        return -1
    else:
        nb = nb.replace("Hplus: ", "")
        return nb

def getSmoins(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Smoins:") == -1):
        return -1
    else:
        nb = nb.replace("Smoins: ", "")
        return nb

def getSplus(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Splus:") == -1):
        return -1
    else:
        nb = nb.replace("Splus: ", "")
        return nb

def getVmoins(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Vmoins:") == -1):
        return -1
    else:
        nb = nb.replace("Vmoins: ", "")
        return nb

def getVplus(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Vplus:") == -1):
        return -1
    else:
        nb = nb.replace("Vplus: ", "")
        return nb

def getLuminosite(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Luminosite:") == -1):
        return -1
    else:
        nb = nb.replace("Luminosite: ", "")
        return nb

def getContraste(fichier):
    l = fichier.readline()
    nb = l
    if(nb.find("Contraste:") == -1):
        return -1
    else:
        nb = nb.replace("Contraste: ", "")
        return nb
