import os as os
import time
from threading import Thread
from tkinter import *

import cv2

import fonctionsFichierProvisoire as fichierProvisoire
import VariableGlobal as varg
from Fenetre import interface
from FonctionsAnnexes import ecrire
from fonctionsFichier import *
from FonctionVisualiser import visualiser
from OuvrirInformationsCalibrations import afficherSource
from Scan import *

valeur = getIntCamera()
if(valeur == -1):
    print("[ERROR] Gros probleme dans la config à camera")
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(valeur)

def debugscan(img):


    scanarr=scan(img)
        
    maskb=viscan(img,scanarr)

    while(True):
        cv2.imshow('DebugScan',maskb)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 13:
            cv2.destroyAllWindows()
            break

class test(Thread):
    def __init__(self):
        Thread.__init__(self)



    def run(self):
        reussite = True
        ret,frame =  cap.read()
        
        time.sleep(1)

        ValeurIndexVue = interface.IndexVue#Variable qui dit qu'elle vu est activé (icimemoire de la vue active)
        ValeurIndexVisualiser = interface.indiceVisualiser
        ValeurVarMoteur = interface.VariableMoteur

        statutTop= 0 #le statut du toplevel
        
        imageCam=varg.photo1 #initialisation image
        
        height=varg.photo1.height()

        varg.scanStart=False

        triggerhsv=True

        
        while(interface.statut!= 0): #interface.statut == 1 quand la fenetre tkinter est ouverte, == 0 quand la fenetre tkinter devient fermée
            #Test si le bouton visualiser est activé !
            if(ValeurIndexVisualiser != interface.indiceVisualiser):
                interface.indiceVisualiser = 0
                if(os.path.isfile("FichierTemporaire.txt")):
                    visualiser()
                else:
                    ecrire("Vous n'avez pas ouvert de fichier", color="retour")
            time.sleep(1/25)
            if(reussite == True):
                if(varg.scanStart==False):
                
                    if(triggerhsv):
                        
                        calib= open("SAVES\precedente_calibrations.txt", "r")

                        hm=int( getHmoins(calib) )
                        hp=int( getHplus(calib) )
                        sm=int( getSmoins(calib) )
                        sp=int( getSplus(calib) )
                        vm=int( getVmoins(calib) )
                        vp=int( getVplus(calib) )

                        
                        triggerhsv = False
                
                    
                    
                    ret,frame =  cap.read()
                    
                    #Test si un des boutons vue est cliqué !
                    if(ValeurIndexVue != interface.IndexVue):

                        ecrire("la vue "+str(interface.IndexVue),color="blue")
                        ValeurIndexVue = interface.IndexVue  

                        
                    #Test si un des boutons Tourner à Gauche / Tourner à droite est cliqué / COnnecter Arduino est cliqué
                    #try except des erreur de serial
                    try : 
                        if(ValeurVarMoteur != interface.VariableMoteur):
                            ecrire("Envoyer comme information: "+interface.VariableMoteur, color="blue")
                            
                            if(interface.VariableMoteur == "000500" ):
                                varg.serial.write(str("000500").encode('utf-8'))
                                
                            if(interface.VariableMoteur == "001500" ):
                                varg.serial.write(str("001500").encode('utf-8'))
                            
                            ecrire("Successful send",color="retour")
                            interface.VariableMoteur=0
                            ValeurVarMoteur = interface.VariableMoteur
                    except AttributeError :
                        ecrire("L'arduino n'est pas connecter ",color="red")
                        interface.VariableMoteur=0
                        ValeurVarMoteur = interface.VariableMoteur
                        
                    
                

                    if(ValeurIndexVue == 1):
                        try:
                            imageCam=convertTk(frame)
                        except AttributeError:
                            reussite=False
                            ecrire("Veuillez séléctionner le port où est branchée la camera puis redemarrez le logiciel", color="error")
                    if(ValeurIndexVue == 2):
                        imageCam=convertTk(threshold(frame,hm,sm,vm,hp,sp,vp))
                    if(ValeurIndexVue == 3):
                        imageCam=convertTk(cv2.bitwise_and(frame,frame, mask= threshold(frame,hm,sm,vm,hp,sp,vp) ))

                    
                    varg.labelPrincipal.configure(image = imageCam)
                    varg.labelPrincipal.image = imageCam #Pour corriger le bug de clignotement
                    
                    if(varg.statutTop!=statutTop):
                        statutTop = varg.statutTop
                        time.sleep(0.1)

                        if (statutTop==0):
                            triggerhsv = True
                        
                        
                    if(varg.statutTop==1):

                        try :
                            try :
                                imagecalib=convertTk(frame)
                                varg.labelVideoNormale.configure(image=imagecalib)
                                varg.labelVideoNormale.image = imagecalib #Pour corriger le bug de clignotement
                                
                                imageModif = threshold(frame, varg.valueHmoins.get() , varg.valueSmoins.get() , varg.valueVmoins.get() , varg.valueHplus.get() , varg.valueSplus.get() , varg.valueVplus.get() )

                                if(os.path.isfile("SAVES\imageFond.jpg")):
                                    fond = cv2.cvtColor(cv2.imread("SAVES\imageFond.jpg"), cv2.COLOR_BGR2GRAY)
                                
                                    imageSoustraite = cv2.subtract(imageModif, fond)
                                    imagetresh= convertTk(imageSoustraite)
                                else:
                                    imagetresh= convertTk(imageModif)
                                varg.labelVideoLaser.configure(image=imagetresh)
                                varg.labelVideoLaser.image=imagetresh #Pour corriger le bug de clignotement
                                if(varg.indicePhoto == 1):
                                    varg.indicePhoto = 0
                                    cv2.imwrite("SAVES\imageFond.jpg", imageModif)
                                    ecrire("Le fond a bien été défini", color="retour")

                                
                            except AttributeError:
                                ecrire("Veuillez séléctionnez le port ou est branchée la camera puis redemarrez le logiciel", color="error")
                        except TclError :
                            varg.statTop = 0
                else:

                    ecrire("Lancement du Scan :",color="retour")
                    ecrire("Nom : "+varg.scanName,color="retour")
                    ecrire("Dans la destination : "+varg.scanLink,color="retour")
                    ecrire("Precision : "+str(varg.scanPrecision),color="retour")
                    ecrire("Temps estimé : "+str(((2048/(varg.scanPrecision))*0.8)/60)+" min",color="retour")

                    ReturnScan = Scanning(cap,1,varg.scanPrecision,hm,sm,vm,hp,sp,vp)

                    FileScan=open(varg.scanLink+".txt","a")
                    FileScan.write(ReturnScan)
                    FileScan.close()
                    afficherSource(varg.scanLink)
                    varg.scanStart=False
        else:
            try:
                fichierProvisoire.delete()
            except FileNotFoundError:
                print("Aucun fichier a supprimer")

interface = interface()
test= test()

interface.start()
test.start()

interface.join()
test.join()
