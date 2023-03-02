from tkinter import *
import datetime
import tkinter.font as tkFont
from functools import partial
from tkinter.filedialog import *
import VariableGlobal as varg
from FonctionsAnnexes import ecrire
from fonctionsFichier import getUSB
import serial
"""
Comme son nom l'indique cette classe est là pour gerer le Fenetre qui se trouve avant et pendant le scan.
Elle a pour but de recupérer les informations essentielles:
-Nom
-Date
-NbDeTours et leurs Hauteurs
-Lien 
"""

class FenetreScan:
    def __init__(self,fenetre):
        top = Toplevel(fenetre)
        top.title("Menu Scan")
        top.resizable(False, False)
        top.grab_set()
        top.transient(fenetre)
        iconfile = "SAVES\images\icone-ConvertImage.ico"
        top.iconbitmap(iconfile)
        police= tkFont.Font(fenetre, size=10, family='Courier')

        #PAGE 3 ========================================================================
        FramePage3 = Frame(top, width =550, height = 150)
        FramePage3.grid_propagate(0)
        FramePage3.grid(row = 1, column = 1)
        FramePage3.grid_remove()

        texte = Text(FramePage3, bg="#EFEFEF", height=9, width = 68)
        texte.grid(sticky="nsew")
        texte.tag_configure("blue", foreground="blue")
        
        
        #PAGE 2 ========================================================================
        FramePage2 = Frame(top, width =550, height = 150)
        FramePage2.grid_propagate(0)
        FramePage2.grid(row = 1, column = 1)
        FramePage2.grid_remove()


        FrameTexte = Frame(FramePage2)
        FrameTexte.grid(row=1,column=1)
        textTour = Label(FrameTexte, text="Tour numéro:", font=police)
        textTour.grid(row = 1, column = 1, padx=15,pady=20)
        textHauteur = Label(FrameTexte, text="Hauteur du Tour:\n(en mm)",font=police)
        textHauteur.grid(row = 2, column = 1,padx=15,pady=20)



        FrameH1 = Frame(FramePage2)
        FrameH1.grid(row=1,column =2)
        FrameH1.grid_remove()
        h1Txt = Label(FrameH1, text="1°", font=police)
        h1Txt.grid(row=1,column =2,pady=20)
        
        h1 = Spinbox(FrameH1, from_=0.0, to=180.0, format='%3.1f',increment=5, justify='right', width=5)
        h1.grid(row = 2, column = 2, padx=15,pady=20)


        FrameH2 = Frame(FramePage2)
        FrameH2.grid(row=1,column =3)
        FrameH2.grid_remove()
        h2Txt = Label(FrameH2, text="2°", font=police)
        h2Txt.grid(row=1,column =3,pady=20)

        h2 = Spinbox(FrameH2, from_=0.0, to=180.0, format='%3.1f',increment=5, justify='right', width=5)
        h2.grid(row = 2, column = 3, padx=15,pady=20)


        FrameH3 = Frame(FramePage2)
        FrameH3.grid(row=1,column =4)
        FrameH3.grid_remove()
        h3Txt = Label(FrameH3, text="3°", font=police)
        h3Txt.grid(row=1,column =4,pady=20)

        h3 = Spinbox(FrameH3, from_=0.0, to=180.0, format='%3.1f',increment=5, justify='right', width=5)
        h3.grid(row = 2, column = 4, padx=15,pady=20)


        FrameH4 = Frame(FramePage2)
        FrameH4.grid(row=1,column =5)
        FrameH4.grid_remove()
        h4Txt = Label(FrameH4, text="4°", font=police)
        h4Txt.grid(row=1,column =5,pady=20)

        h4 = Spinbox(FrameH4, from_=0.0, to=180.0, format='%3.1f',increment=5, justify='right', width=5)
        h4.grid(row = 2, column = 5, padx=15,pady=20)



        FrameH5 = Frame(FramePage2)
        FrameH5.grid(row=1,column =6)
        FrameH5.grid_remove()
        h5Txt = Label(FrameH5, text="5°", font=police)
        h5Txt.grid(row=1,column =6,pady=20)

        h5 = Spinbox(FrameH5, from_=0.0, to=180.0, format='%3.1f',increment=5, justify='right', width=5)
        h5.grid(row = 2, column = 6, padx=15,pady=20)

        
        #PAGE 1 ========================================================================
        FramePage1 = Frame(top, width =550, height = 150)
        FramePage1.grid_propagate(0)
        
        FrameParametre = LabelFrame(FramePage1, text="Parametres du scan", padx=10,pady=10)
        FrameNom = Frame(FrameParametre)
        FrameDate = Frame(FrameParametre)
        FramePrecision = Frame(FrameParametre)
        FrameAngle = Frame(FrameParametre)
        FrameNbHauteur = Frame(FrameParametre)
        FrameDistance = Frame(FrameParametre)
        FrameEnregistrer = Frame(FramePage1)
        FrameSuivant = Frame(top)
        
        textNom = Label(FrameNom, text="Nom:")
        textNom.grid(row = 1, column = 1)
        nom = StringVar() 
        nom.set("MonScan")
        caseNom = Entry(FrameNom, textvariable=nom, width=41)
        caseNom.grid(row = 1, column = 2)

        textHauteur = Label(FrameNbHauteur, text="Nombre de tours effectués:")
        textHauteur.grid(row = 1, column = 1)

        ChoixNbHauteur = Spinbox(FrameNbHauteur, from_=1, to=5)
        ChoixNbHauteur.grid(row = 1, column = 2)




        textDistance = Label(FrameDistance, text="Distance Camera-Plateau (cm):")
        textDistance.grid(row = 1, column = 1)

        ChoixDistance = Spinbox(FrameDistance, from_=1.0, to=80.0,width='17')
        ChoixDistance.grid(row = 1, column = 2)

        textPrecision = Label(FramePrecision, text="Précision:")
        textPrecision.grid(row = 1, column = 1)

        ChoixNbPrecision = Spinbox(FramePrecision, from_=1, to=2000)
        ChoixNbPrecision.grid(row = 1, column = 2)


        textAngle = Label(FrameAngle, text="Angle camera-Laser:")
        textAngle.grid(row = 1, column = 1)

        ChoixAngle = Spinbox(FrameAngle, from_=1, to=360)
        ChoixAngle.grid(row = 1, column = 2)
        
        dateReel = datetime.datetime.now()
        textDate = Label(FrameDate, text="Date: ")
        textDate.grid(row = 1, column = 1)
        date = StringVar()
        
        #juste pour raouter le 0 devant
        if(dateReel.day <10):
            if(dateReel.month <10):
                date.set("0"+str(dateReel.day)+"/0"+str(dateReel.month)+"/"+str(dateReel.year))
            else:
                date.set("0"+str(dateReel.day)+"/"+str(dateReel.month)+"/"+str(dateReel.year))
        elif(dateReel.month <10):
            date.set(str(dateReel.day)+"/0"+str(dateReel.month)+"/"+str(dateReel.year))
        else:
            date.set(str(dateReel.day)+"/"+str(dateReel.month)+"/"+str(dateReel.year))
        caseDate = Entry(FrameDate, textvariable=date, width=41)
        caseDate.grid(row = 1, column = 2)

        textEnregistrer = Label(FrameEnregistrer, text="Enregistrer sous...")
        textEnregistrer.grid(row = 1, column = 1)
        lien = StringVar() 
        lien.set("direction")
        caseEnregistrer = Entry(FrameEnregistrer, textvariable=lien, width=70)
        caseEnregistrer.grid(row = 1, column = 2)
        boutonEnregistrer = Button(FrameEnregistrer, text="...", command=partial(self.enregistrerScan,lien))
        boutonEnregistrer.grid(row=1, column = 3)

        
        FrameNom.grid(row = 1, column = 1, sticky='w')
        FrameDate.grid(row=2, column=1, sticky='w')
        FrameNbHauteur.grid(row = 3, column =1, sticky='w')
        FrameDistance.grid(row = 4, column =1, sticky='w')
        FramePrecision.grid(row=3,column = 2, sticky='w')
        FrameAngle.grid(row=4,column = 2, sticky='w',padx=2)
        FrameEnregistrer.grid(row = 2, column =1, sticky='w')
        FrameParametre.grid(row = 1, column = 1, sticky='we')
        FrameSuivant.grid(row = 2, column = 1, sticky='e')
        FramePage1.grid(row = 1, column = 1, sticky='we')

        #Bouton commun aux 3 pages
        self.idP = 1
        idPage = StringVar()
        idPage.set("Page 1/3:")
        textPage = Label(FrameSuivant, textvariable=idPage)
        textPage.grid(row = 1, column = 1, sticky='e')
        boutonSuivant = Button(FrameSuivant, text="Suivant")
        boutonSuivant.grid(row=1, column = 3)
        boutonSuivant.config(command=partial(self.suivant,fenetre, top, FramePage1,FramePage2,FramePage3, nom, date, lien, ChoixNbHauteur,ChoixNbPrecision,ChoixDistance,ChoixAngle, idPage, FrameH1, FrameH2, FrameH3, FrameH4, FrameH5,h1,h2,h3,h4,h5,boutonSuivant, texte))
        boutonRetour = Button(FrameSuivant, text="Retour")
        boutonRetour.grid(row=1, column = 2)
        boutonRetour.config(command = partial(self.retour,top, FramePage1,FramePage2,FramePage3, idPage, nom, date, lien, ChoixNbHauteur,ChoixNbPrecision,ChoixDistance,ChoixAngle, FrameH1, FrameH2, FrameH3, FrameH4, FrameH5,h1,h2,h3,h4,h5,boutonSuivant))
    
    """
    Cette fonction s'execute avec le bouton ... de enregistrer sous
    elle permet de connaitre le lien vers le futur fichier (celui que l'on cree à la fin
    """
    def enregistrerScan(self,lien): #liste = listes de toutes les hauteurs
        filename = asksaveasfilename(title="Enregistrer votre scan",filetypes=[('txt files','.txt'),('all files','.*')])
        lien.set(filename)
        
    """
    Fonction qui gere le bouton retour de la fenetre
    Son role est de faire apparaitre ou disparaitre les pages à l'inverse de suivant (en gros)
    """
    def suivant(self,fenetre,top, FramePage1, FramePage2, FramePage3, caseNom, caseDate, caseEnregistrer, ChoixNbHauteur,ChoixNbPrecision,ChoixDistance,ChoixAngle,idPage, FrameH1, FrameH2, FrameH3, FrameH4, FrameH5,h1,h2,h3,h4,h5,boutonSuivant, texte):
        if(self.idP == 3):

            val = 0 #Passe à 1 Si les valeurs des hauteurs sont bonnes
            if(len(varg.scanTours) == 1):
                if(float(varg.scanTours[0]) >= 0 and float(varg.scanTours[0]) <180):
                    val = 1
            elif(len(varg.scanTours) == 2):
                if(float(varg.scanTours[0]) >= 0 and float(varg.scanTours[0]) <180 and float(varg.scanTours[1]) >= 0 and float(varg.scanTours[1]) <180):
                    val = 1
            elif(len(varg.scanTours) == 3):
                if(float(varg.scanTours[0]) >= 0 and float(varg.scanTours[0]) <180 and float(varg.scanTours[1]) >= 0 and float(varg.scanTours[1]) <180 and float(varg.scanTours[2]) >= 0 and float(varg.scanTours[2]) <180):
                    val = 1
            elif(len(varg.scanTours) == 4):
                if(float(varg.scanTours[0]) >= 0 and float(varg.scanTours[0]) <180 and float(varg.scanTours[1]) >= 0 and float(varg.scanTours[1]) <180 and float(varg.scanTours[2]) >= 0 and float(varg.scanTours[2]) <180 and float(varg.scanTours[3]) >= 0 and float(varg.scanTours[3]) <180):
                    val = 1
            elif(len(varg.scanTours) == 5):
                if(float(varg.scanTours[0]) >= 0 and float(varg.scanTours[0]) <180 and float(varg.scanTours[1]) >= 0 and float(varg.scanTours[1]) <180 and float(varg.scanTours[2]) >= 0 and float(varg.scanTours[2]) <180 and float(varg.scanTours[3]) >= 0 and float(varg.scanTours[3]) <180 and float(varg.scanTours[4]) >= 0 and float(varg.scanTours[4]) >180):
                    val = 1
            if(val == 0):
                ecrire("Il y a une erreur dans le nombre de tours à effectuer ou dans les hauteurs de chaque tours. Pour rappel la hauteur doit etre dans l'intervalle [0 ; 180]", color="error")
            else:
                #Verification que tout est bon
                """
                ======================================================================================================
                A RAJOUTER LE TEST DE LA CAMERA
                ======================================================================================================
                """
                try:
                        #Lancement du scan
                        fichier = open(varg.scanLink+".txt", "w")
                        fichier.write("nom: "+varg.scanName+"\ndate: "+varg.scanDate+"\nprecision: "+str(varg.scanPrecision)+"\ndistance: "+str(ChoixDistance.get())+"\nangle: "+ChoixAngle.get()+"\nnbTours: "+str(len(varg.scanTours))+"\n")
                        if(len(varg.scanTours) >= 1):
                            fichier.write("H: "+varg.scanTours[0]+"\n")
                        if(len(varg.scanTours) >= 2):
                            fichier.write("H: "+varg.scanTours[1]+"\n")
                        if(len(varg.scanTours) >= 3):
                            fichier.write("H: "+varg.scanTours[2]+"\n")
                        if(len(varg.scanTours) >= 4):
                            fichier.write("H: "+varg.scanTours[3]+"\n")
                        if(len(varg.scanTours) >= 5):
                            fichier.write("H: "+varg.scanTours[4]+"\n")
                        fichier.close()
                        top.destroy()
                        ecrire("Fichier Scan crée avec succès, début de scan", color="retour")
                        # recuperation main :
                        varg.scanStart=True
                    
                    
                except FileNotFoundError :
                    ecrire("Vous avez encore une erreur, verifier que le lien d'enregistrement est correct", color="error")
            
        if(self.idP ==2):
            FramePage2.grid_remove()
            
            try:
                varg.scanTours[0]=h1.get()
                varg.scanTours[1]=h2.get()
                varg.scanTours[2]=h3.get()
                varg.scanTours[3]=h4.get()
                varg.scanTours[4]=h5.get()
            except IndexError:
                pass
            
            FramePage3.grid()
            texte.configure(state="normal")
            texte.delete(1.0, END)
            texte.insert(END, " >>> Informations sur le scan:\n","blue")
            texte.insert(END, " Nom: "+varg.scanName+"\n")
            texte.insert(END, " Date: "+varg.scanDate+"\n")
            texte.insert(END, " Lien d'enregistrement: "+varg.scanLink+"\n")
            texte.insert(END, " Nombre de Scan a effectuer: "+str(len(varg.scanTours))+"\n")
            texte.insert(END, " Précision: "+str(varg.scanPrecision)+"\n")
            texte.insert(END, " Distance: "+str(ChoixDistance.get())+"\n")
            texte.insert(END, " >>> Si tout est bon, que vous avez positionné votre objet sur le\n scanner alors cliquez sur \"lancer le scan\" !", "blue")
            texte.configure(state="disabled")
            idPage.set("Page 3/3:")
            boutonSuivant.config(text="Lancer le Scan")
            #le compteur de page
            self.idP =self.idP+1

        if(self.idP == 1):
            #On enregistre nos données dans nos variables globales
            varg.scanName = caseNom.get()
            varg.scanDate = caseDate.get()
            varg.scanLink = caseEnregistrer.get()

            try:
                varg.scanTours = [""]*int(ChoixNbHauteur.get())
                varg.scanPrecision = int(ChoixNbPrecision.get())
                FramePage1.grid_remove()
                FramePage2.grid()
                
                idPage.set("Page 2/3:")
                
                if(len(varg.scanTours) == 1):
                    FrameH1.grid()
                    FrameH2.grid_remove()
                    FrameH3.grid_remove()
                    FrameH4.grid_remove()
                    FrameH5.grid_remove()
                elif(len(varg.scanTours) == 2):
                    FrameH1.grid()
                    FrameH2.grid()
                    FrameH3.grid_remove()
                    FrameH4.grid_remove()
                    FrameH5.grid_remove()
                elif(len(varg.scanTours) == 3):
                    FrameH1.grid()
                    FrameH2.grid()
                    FrameH3.grid()
                    FrameH4.grid_remove()
                    FrameH5.grid_remove()
                elif(len(varg.scanTours) == 4):
                    FrameH1.grid()
                    FrameH2.grid()
                    FrameH3.grid()
                    FrameH4.grid()
                    FrameH5.grid_remove()
                elif(len(varg.scanTours) == 5):
                    FrameH1.grid()
                    FrameH2.grid()
                    FrameH3.grid()
                    FrameH4.grid()
                    FrameH5.grid()
                else:
                    ecrire("Vous n'avez pas rentré une valeur correcte dans Nombre de Tours", color="error")
                #le compteur de page
                self.idP =self.idP+1
            except ValueError:
                ecrire("Vous devez mettre un nombre entier dans Hauteur et Precision")

    """
    Fonction qui gere le bouton retour de la fenetre
    Son role est de faire apparaitre ou disparaitre les pages à l'inverse de suivant (en gros)
    """
    def retour(self,top, FramePage1, FramePage2, FramePage3, idPage, nom, date, lien, ChoixNbHauteur,ChoixNbPrecision,ChoixDistance,ChoixAngle, FrameH1, FrameH2, FrameH3, FrameH4, FrameH5,h1,h2,h3,h4,h5,boutonSuivant):
        if(self.idP == 1):
            top.destroy()
        if(self.idP == 2):
            FramePage2.grid_remove()
            FramePage1.grid()
            idPage.set("Page 1/3:")
            
        if(self.idP == 3):
            idPage.set("Page 2/3:")
            boutonSuivant.config(text="Suivant")
            FramePage3.grid_remove()
            FramePage2.grid()
            idPage.set("Page 2/3:")
            if(len(varg.scanTours) == 1):
                FrameH1.grid()
                FrameH2.grid_remove()
                FrameH3.grid_remove()
                FrameH4.grid_remove()
                FrameH5.grid_remove()
            elif(len(varg.scanTours) == 2):
                FrameH1.grid()
                FrameH2.grid()
                FrameH3.grid_remove()
                FrameH4.grid_remove()
                FrameH5.grid_remove()
            elif(len(varg.scanTours) == 3):
                FrameH1.grid()
                FrameH2.grid()
                FrameH3.grid()
                FrameH4.grid_remove()
                FrameH5.grid_remove()
            elif(len(varg.scanTours) == 4):
                FrameH1.grid()
                FrameH2.grid()
                FrameH3.grid()
                FrameH4.grid()
                FrameH5.grid_remove()
            elif(len(varg.scanTours) == 5):
                FrameH1.grid()
                FrameH2.grid()
                FrameH3.grid()
                FrameH4.grid()
                FrameH5.grid()
            else:
                ecrire("Vous avez encore laissé de la merde dans Nombre de Tours bandes de petits fdp qui ne m'écoutent pas", color="error")

        #le compteur de page
        if(self.idP == 2 or self.idP == 3):
            self.idP =self.idP-1

