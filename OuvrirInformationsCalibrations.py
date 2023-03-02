from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showerror, askokcancel
from FonctionsAnnexes import ecrire
from fonctionsFichier import *
import tkinter.font as tkFont
from functools import partial
import VariableGlobal as varg
import fonctionsFichierProvisoire as fichierProvisoire

"""
Fonction qui enleve les fichier importées
"""
def nouveau():
    varg.labelSource.set("- Aucun fichier n'est actuellement importé")
    fichierProvisoire.delete()
"""
Fonction qui importe un fichier déjà scanné
"""
def ouvrir():
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
    afficherSource(filename)

def afficherSource(filename):
    try:
        fichier = open(filename, "r")
        nom = getNom(fichier)
        date = getDate(fichier)
        precision = getPrecision(fichier)
        distance = getDistance(fichier)
        angle = getAngle(fichier)
        nbTours = getNbTours(fichier)
        if(nom == "ERROR01" or date== 'ERROR01' or nbTours == "ERROR01"or precision == "ERROR01" or distance =="ERROR01"):
            ecrire("Fichier inconnu",color="error")
            fenetreErreur("Le fichier est illisible:\nIl peut ne pas s'agir d'un fichier de scan ou ce dernier a été manuellement modifié\n\nNous vous recommandons de verifier que vous avez ouvert le bon fichier sinon de refaire le scan de l'objet")
        else:
            varg.labelSource.set("- "+nom+"\n"+"   -Date: "+date+"\n"+"   -Précision: "+precision+"\n"+"   -Distance: "+distance+"\n"+"   -Nombre de Scan effectués: "+nbTours)
            ecrire("Fichier ouvert avec succès", color="reponse")
            fichierProvisoire.edit(filename)
        fichier.close()
    except FileNotFoundError:
        pass

"""
Fonction qui donne des infos
"""
def informations(fenetre):
    top = Toplevel(fenetre)
    top.title("Informations")
    top.resizable(False, False)
    top.transient(fenetre)
    iconfile = "SAVES\images\icone-ConvertImage.ico"
    top.iconbitmap(iconfile)
    fichier = open("SAVES\informations.txt", "r")
    label1 = Label(top, text=fichier.read(),wraplength=400, justify='left', bg="#f8e7d3",padx=3, pady=5).pack(side=TOP)

    Button(top, text="Retour", command= top.destroy, activeforeground="red").pack(side=BOTTOM, padx=5,pady=5)
    fichier.close()



    
"""
Fonction qui gere la fenetre calibration
"""

class calibrationFenetre:
    
    def __init__(self, fenetre):

        #Police des boutons(en bas de la page de calibrations
        police= tkFont.Font(fenetre, size=15, family='Arial')
        policeMoyenne= tkFont.Font(fenetre, size=13, family='Arial')

        #Parametre de la fenetre de calibrations
        top = Toplevel(fenetre)
        top.title("Calibrations")
        top.resizable(False, False)
        top.transient(fenetre)
        
        iconfile = "SAVES\images\icone-ConvertImage.ico"
        top.iconbitmap(iconfile)
        #Le statut de la fenetre
        varg.statutTop = 1

        #Listes des differentes Frames
        FrameCameraNormale = LabelFrame(top, text="Vue de la Webcam")
        FrameConfig = Frame(top)
        FrameCameraLigne = LabelFrame(top, text="Camera laser")
        FrameBouton = Frame(top)


        """
        ici les cameras
        """
        varg.labelVideoNormale = Label(FrameCameraNormale,image=varg.photo1)
        varg.labelVideoNormale.grid()


        varg.labelVideoLaser = Label(FrameCameraLigne,image=varg.photo1)
        varg.labelVideoLaser.grid()


        #Les valeurs et les scales:

        varg.valueHmoins = IntVar(top)
        scaleHmoins = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Hue -', variable=varg.valueHmoins, tickinterval=255, orient='h',length =5*50/2,sliderlength=15)
        scaleHmoins.grid(row=1, column =1)

        varg.valueHplus = IntVar(top)
        scaleHplus = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Hue +', variable=varg.valueHplus, tickinterval=255, orient='h',length =5*50/2,sliderlength=15)
        scaleHplus.grid(row=1, column =2)


        varg.valueSmoins = IntVar(top)
        scaleSmoins = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Saturation -', variable=varg.valueSmoins, tickinterval=255, orient='h',length =5*50/2,sliderlength=15)
        scaleSmoins.grid(row=2, column =1)

        varg.valueSplus = IntVar(top)
        scaleSplus = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Saturation +', variable=varg.valueSplus, tickinterval=255, orient='h',length =5*50/2,sliderlength=15)
        scaleSplus.grid(row=2, column =2)

        varg.valueVmoins = IntVar(top)
        scaleVmoins = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Value -', variable=varg.valueVmoins, tickinterval=255, orient='h', length =5*50/2,sliderlength=15)
        scaleVmoins.grid(row=3, column =1)

        varg.valueVplus = IntVar(top)
        scaleVplus = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Value +', variable=varg.valueVplus, tickinterval=255, orient='h', length =5*50/2,sliderlength=15)
        scaleVplus.grid(row=3, column =2)

        valueLuminosite = IntVar(top)
        scaleLuminosite = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Luminosite', variable=valueLuminosite, tickinterval=255, orient='h', length =5*50,sliderlength=15)
        scaleLuminosite.grid(row=4, column =1, columnspan=2)

        valueContraste = IntVar(top)
        scaleContraste = Scale(FrameConfig, from_=0, to=255, showvalue=True, label='Contraste', variable=valueContraste, tickinterval=255, orient='h', length =5*50,sliderlength=15)
        scaleContraste.grid(row=5, column =1,columnspan=2)

        boutonFond = Button(FrameConfig, text="Definir l'image actuelle\ncomme le fond",font=policeMoyenne,command=self.photo, padx=35, pady=5, relief= 'ridge', borderwidth=5, bg="#e2e2e2")
        boutonFond.grid(row=6,column=1,columnspan=2,padx=2)


        #Gestion des fichiers de calibrations avec entrée de données
        if(os.path.isfile("SAVES\precedente_calibrations.txt")):
            fichier = open("SAVES\precedente_calibrations.txt")

            ouvertureFichier(fichier, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste)

            fichier.close()
        elif(os.path.isfile("SAVES\default_calibrations.txt")):
            fichier = open("SAVES\default_calibrations.txt")

            ouvertureFichier(fichier, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste)

            fichier.close()
        else:
            ecrire("Fichier de calibrations indisponible", color="error")



        #Listes des boutons en bas de la page de calibrations
        boutonReinitialiser = Button(FrameBouton, bg="#e2e2e2", text="Reinitialiser avec les\nparametres d'origines", command=partial(reinitialiser, fichier, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste),padx= 30, pady=5, font=police)
        boutonReinitialiser.grid(row=1, column=1, padx=5)

        boutonImporter = Button(FrameBouton, text="Importer", bg="#e2e2e2", command=partial(importer,scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste),padx= 80, pady=16.49,font=police)
        boutonImporter.grid(row=1, column=2, padx=5)

        boutonEnregistrer = Button(FrameBouton, text="Enregistrer les modifications", command=partial(enregistrerCalibrations, fichier, top, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste),padx= 30, pady=16.49,font=police, bg='green')
        boutonEnregistrer.grid(row=1, column=3, padx=5)

        boutonAnnuler = Button(FrameBouton, text="Annuler", bg="#e2e2e2", command=partial(destroy , top) ,padx= 80, pady=16.49,font=police)
        boutonAnnuler.grid(row=1, column=4, padx=5)

        boutonExporter = Button(FrameBouton, bg="#e2e2e2", text="Exporter les calibrations\nactuelles dans un fichier", command=partial(exporterCalibrations, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste), padx= 30, pady=5,font=police)
        boutonExporter.grid(row=1, column=5, padx=5)



        #Affichage des Frames
        FrameBouton.grid(row=2, column=1, columnspan=3, pady=3)
        FrameCameraNormale.grid(row=1, column=1)
        FrameConfig.grid(row=1, column=2)
        FrameCameraLigne.grid(row=1, column=3)

        ##top.mainloop()
        ##varg.statutTop = 0

    def photo(self):
        varg.indicePhoto = 1


#--------------------------------------------------------------------------------------------------------------
#Fin de la fonction Calibrations
#--------------------------------------------------------------------------------------------------------------
"""
Fonction destroy topLevel
"""

def destroy(top):
    top.destroy()
    varg.statutTop = 0

"""
Fonction execute lorsqu'on clique sur exporter les calibrations\nactuelles dans un fichier
"""
def exporterCalibrations(scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste):
    filename = asksaveasfilename(title="Enregistrer votre fichier de Calibrations",filetypes=[('txt files','.txt'),('all files','.*')])
    fichier = open(filename+".txt", "w")
    fichier.write("Hmoins: "+str(scaleHmoins.get())+"\nHplus: "+str(scaleHplus.get())+"\nSmoins: "+str(scaleSmoins.get())+"\nSplus: "+str(scaleSplus.get())+"\nVmoins: "+str(scaleVmoins.get())+"\nVplus: "+str(scaleVplus.get())+"\nLuminosite: "+str(scaleLuminosite.get())+"\nContraste: "+str(scaleContraste.get()))
    fichier.close()
    
"""
Fonctions qui s'execute lorsqu'on clique sur le bouton enregistrer dans la fenetre Calibrations
Elle enregistre les paramatres actuels dans le fichier precedente_calibrations.txt et le cree s'il n'existe pas
"""

def enregistrerCalibrations(fichier, top,scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste):
    if(os.path.isfile("SAVES\precedente_calibrations.txt")):
        fichier = open("SAVES\precedente_calibrations.txt","w")
        fichier.write("Hmoins: "+str(scaleHmoins.get())+"\nHplus: "+str(scaleHplus.get())+"\nSmoins: "+str(scaleSmoins.get())+"\nSplus: "+str(scaleSplus.get())+"\nVmoins: "+str(scaleVmoins.get())+"\nVplus: "+str(scaleVplus.get())+"\nLuminosite: "+str(scaleLuminosite.get())+"\nContraste: "+str(scaleContraste.get()))
        #ouvertureFichier(fichier, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste)

        fichier.close()
        ecrire("Les Calibrations ont bien été enregistrées",color="reponse")
    else:
        #create le fichier et enregistrer les paramettres
        fichier = open("SAVES\precedente_calibrations.txt","w")
        fichier.write("Hmoins: "+str(scaleHmoins.get())+"\nHplus: "+str(scaleHplus.get())+"\nSmoins: "+str(scaleSmoins.get())+"\nSplus: "+str(scaleSplus.get())+"\nVmoins: "+str(scaleVmoins.get())+"\nVplus: "+str(scaleVplus.get())+"\nLuminosite: "+str(scaleLuminosite.get())+"\nContraste: "+str(scaleContraste.get()))
        fichier.close()
        ecrire("Les Calibrations ont bien été enregistrées",color="reponse")
    destroy(top)
"""
Fonctions execute lorsqu'on clique sur le bouton importer dans la fenetre Calibrage
"""
class importer():
    def __init__(self, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste):
        filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
        try:
            self.fichier = open(filename, "r")

            ouvertureFichier(self.fichier, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste)
        
            self.fichier.close()
        except FileNotFoundError:
            print("Erreur traité: FileNotFoundError")


"""
Fonctions execute lorsqu'on clique sur le bouton reinitialiser dans la fenetre Calibrage
"""
def reinitialiser(fichier, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste):
    if(os.path.isfile("SAVES\default_calibrations.txt")):
        fenetre = Tk()
        fenetre.withdraw()
        if(askokcancel("Attention", "Reinitialiser les parametres ? ", default="cancel")):
            fichier = open("SAVES\default_calibrations.txt")
            ouvertureFichier(fichier, scaleHmoins, scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste)
            fichier.close()
            ecrire("Les parametres de calibration ont bien été réinitialisés.", color="reponse")
        fenetre.destroy()
    else:
        fenetreErreur("Impossible de reinitialiser les parametres par default car le fichier est introuvable ou erroné")
        ecrire("Impossible de reinitialiser les parametres par default car le fichier est introuvable ou erroné", color="error")
    



"""
Est executé pour ouvrir les fichiers de calibrations (economise de la place dans la fonction calibrations()
"""
def ouvertureFichier(fichier, scaleHmoins,scaleHplus, scaleSmoins, scaleSplus, scaleVmoins, scaleVplus, scaleLuminosite, scaleContraste):
    Hmoins = getHmoins(fichier)
    Hplus = getHplus(fichier)

    Smoins = getSmoins(fichier)
    Splus = getSplus(fichier)

    Vmoins = getVmoins(fichier)
    Vplus = getVplus(fichier)

    luminosite = getLuminosite(fichier)

    contraste = getContraste(fichier)

    if(Hmoins==-1 or Hplus==-1 or Smoins==-1 or Splus==-1 or Vmoins==-1 or Vplus==-1 or luminosite==-1 or contraste==-1):
        ecrire("Le fichier est illisible:Il peut ne pas s'agir d'un fichier de scan ou ce dernier a été manuellement modifié. Nous vous recommandons de verifier que vous avez ouvert le bon fichier sinon de refaire le scan de l'objet", color="error")
        fenetreErreur("Le fichier est illisible:\nIl peut ne pas s'agir d'un fichier de scan ou ce dernier a été manuellement modifié\n\nNous vous recommandons de verifier que vous avez ouvert le bon fichier sinon de refaire le scan de l'objet")
    else:
        scaleHmoins.set(Hmoins)
        scaleHplus.set(Hplus)
        scaleSmoins.set(Smoins)
        scaleSplus.set(Splus)
        scaleVmoins.set(Vmoins)
        scaleVplus.set(Vplus)
        scaleLuminosite.set(luminosite)
        scaleContraste.set(contraste)







"""
Fait apparaitre une fenetre d'erreur déjà prédefinie
"""
def fenetreErreur(text):
    fenetre = Tk()
    fenetre.withdraw()
    showerror("Erreur d'importation du fichier", text)
    fenetre.destroy()
