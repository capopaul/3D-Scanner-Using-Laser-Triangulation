from tkinter import *
from threading import Thread
from OuvrirInformationsCalibrations import *
from functools import partial
import VariableGlobal as varg
import serial
from FonctionsAnnexes import ecrire
from FenetreScan import FenetreScan

#Classe lancée lors du démarrage du logiciel dans le main
class interface(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):

        #initialisation des differentes variables
        self.VariableMoteur =0
        self.indiceVisualiser = 0
        self.IndexVue = 1
        self.statut = 1 #est une variable qui passe sur 0 seulement quand la fenetre est fermée
        self.statutTop = 0


        #création de la fenetre TKinter
        fenetre = Tk()
        iconfile = "SAVES\images\icone-ConvertImage.ico"
        fenetre.iconbitmap(iconfile)
        
        #Listes des polices à utiliser
        police= tkFont.Font(fenetre, size=20, family='Courier')
        policePetite= tkFont.Font(fenetre, size=15, family='Courier')
        policeGrande= tkFont.Font(fenetre, size=30, family='Courier')


        #Les des Frames qui organisent mon image
        FrameSource = LabelFrame(fenetre, text="Sources: ", bg="#e2e2e2")
        FrameBouton = LabelFrame(fenetre, text="Listes des differents effects",bg="#A0A0A0", padx=38)
        FrameConsole = Frame(fenetre, bg="#EBEBEB", relief='groove',borderwidth ='2')
        FrameCamera = Frame(fenetre, bg="white")
        FrameDroite = Frame(fenetre, bg="#e2e2e2")
        """A adater selon l'image   le pady a 88"""

        #Affichage des frames
        FrameSource.grid(row=1,column = 1, sticky="nesw")
        FrameBouton.grid(row=2, column=1, rowspan=2, sticky="ns")
        FrameCamera.grid(row=1, column=2, rowspan=2, sticky="nesw")
        FrameConsole.grid(row=3, column=2, sticky="nesw", padx=3)
        FrameDroite.grid(row=1, column=3, rowspan=3, sticky="ns")

        #Sources
        varg.labelSource = StringVar()
        texteSource = Label(FrameSource, textvariable=varg.labelSource, wraplength=190, justify=LEFT, bg='#e2e2e2')
        varg.labelSource.set("- Aucun fichier n'est actuellement importé")
        texteSource.grid(sticky="nesw")

        
        #En dessous on trouve la vidéo
        
        varg.photo1 = PhotoImage(file="SAVES\images\ImageFond.gif")

        varg.labelPrincipal = Label(FrameCamera, image = varg.photo1)
        varg.labelPrincipal.grid()

        #Parametre de la console
        titreFrame = Label(FrameConsole, text="Informations et Messages d'erreurs :", bg="#EBEBEB")
        titreFrame.grid(row=1, column = 1, sticky="w")

        ScrollBarY = Scrollbar(FrameConsole, orient="vertical")
        ScrollBarY.grid(row = 2, column = 2, sticky='ns')


        varg.console = Text(FrameConsole, yscrollcommand =ScrollBarY.set, bg="White",height=7, width=76)
        varg.console.tag_configure("red", foreground="red")
        varg.console.tag_configure("blue", foreground="blue")
        varg.console.tag_configure("black", foreground="black")
        ecrire("Branchez le scanner, puis cliquez sur le bouton Connecter  (a droite de l ecran)", color="black")
        varg.console.grid(row = 2, column = 1, sticky= "nswe",pady=5)

        ScrollBarY.config(command=varg.console.yview)
        varg.console.yview("scroll", 1000, "units")

        #Listes des boutons qui permettent de changer de vues

        boutonVue1 = Button(FrameBouton, text="Vue 1", command=partial(self.vue, 1), padx= 20, pady=5, bg="#e2e2e2")
        boutonVue1.grid(row=1, ipadx= 15, pady = 15)
        boutonVue2 = Button(FrameBouton, text="Vue 2", command=partial(self.vue, 2), padx= 20, pady=5, bg="#e2e2e2")
        boutonVue2.grid(row=2, ipadx= 15, pady = 15)
        boutonVue3 = Button(FrameBouton, text="Vue 3", command=partial(self.vue, 3), padx= 20, pady=5, bg="#e2e2e2")
        boutonVue3.grid(row=3, ipadx= 15, pady = 15)

        #Boutons de Scan et Visualisation + Arduino
        MiniFrameScanVisu = Frame(FrameDroite, bg="#A0A0A0", relief='groove',borderwidth ='2')#C3C7F6
        MiniFrameScanVisu.grid(row=1, column=1)
        
        boutonScan = Button(MiniFrameScanVisu, text="Scanner", bg="#e2e2e2",font= police,command=partial(lancerScan,fenetre), width= 11, padx= 0, pady=50)
        boutonScan.grid(padx= 35, pady=30)
        boutonVisualiser = Button(MiniFrameScanVisu, text="Visualiser",bg="#e2e2e2", command=partial(self.Visualiser, 1), font=police, width= 11, pady=50)
        boutonVisualiser.grid(padx= 15, pady=30)

        #Partie Arduino
        FrameArduino = LabelFrame(FrameDroite,text="ArduinoConfig" ,bg="#e2e2e2")


        #           Lier à la camera:
        texteCamera = Label(FrameArduino, text="Port Camera:",bg="#e2e2e2")
        texteCamera.grid(row=1,column =1, sticky="w")

        ValeurCamera = Label(FrameArduino, bg="gray", width=5,justify='right')
        ValeurCamera.grid(row=1,column=2, sticky="w")
        intCamera = getIntCamera()
        if(intCamera != -1):
            ValeurCamera.configure(text=intCamera)
        else:
            ValeurCamera.configure(text="Null")

        intEntryCamera = StringVar()
        EntryCamera = Entry(FrameArduino,textvariable=intEntryCamera,width=7,justify ='right')
        EntryCamera.grid(row=1,column=3, sticky="w")


        valider = PhotoImage(file="SAVES/images/valider.png")
        ValideCamera = Button(FrameArduino, image =valider, command=partial(self.validerCamera, EntryCamera, ValeurCamera,intEntryCamera))
        ValideCamera.grid(row=1,column=4)

        #         lier à l'usb
        texteUsb = Label(FrameArduino, text="Port Usb:",bg="#e2e2e2")
        texteUsb.grid(row=2,column =1,pady=2, sticky="w")
        
        ValeurUsb = Label(FrameArduino, bg="gray",width=5,justify='right')
        ValeurUsb.grid(row=2,column=2, sticky="w")
        intUsb = getUSB()
        if(intUsb != "ERROR01"):
            ValeurUsb.configure(text=intUsb.replace("\n",""))
        else:
            ValeurUsb.configure(text="Null")

        intEntryUsb = StringVar()
        EntryUsb = Entry(FrameArduino,textvariable=intEntryUsb,width=7,justify ='right')
        EntryUsb.grid(row=2,column=3, sticky="w")

        ValideUsb = Button(FrameArduino, image =valider, command=partial(self.validerUsb, EntryUsb, ValeurUsb,intEntryUsb))
        ValideUsb.grid(row=2,column=4)

         #         lier à blender
        texteBlender = Label(FrameArduino, text="Lien vers blender:",bg="#e2e2e2")
        texteBlender.grid(row=3,column =1,pady=2, sticky="w")
        
        lien = StringVar()
        if(getBlender() == "ERROR01"):
            lien.set("blender.exe")
        else:
            lien.set(getBlender())
        caseEnregistrer = Entry(FrameArduino, textvariable=lien, width=20)
        caseEnregistrer.grid(row = 3, column = 2,pady=2, sticky="w",columnspan=2)
        boutonEnregistrer = Button(FrameArduino, text="...", command=partial(self.linkBlender,lien))
        boutonEnregistrer.grid(row=3, column = 4,padx=4)
        

        #Bouton commande moteur

        FlecheHaut = PhotoImage(file="SAVES\images\FlecheHaut.png")
        FlecheDroite = PhotoImage(file="SAVES\images\FlecheDroite.png")
        FlecheGauche = PhotoImage(file="SAVES\images\FlecheGauche.png")
        FlecheBas = PhotoImage(file="SAVES\images\FlecheBas.png")
        
        self.boutonConnecter = Button(FrameArduino, text="Connecter", font=policePetite, command=self.AttemptSerial, bg="#A0A0A0", width= 14, pady=5)
        self.boutonConnecter.grid(row=4, column=1, columnspan=4, padx=15,pady=6)
        
        MiniFrameBoutons = Frame(FrameArduino,bg="#e2e2e2")
        
        boutonTournerMoteurSens1 = Button(MiniFrameBoutons, image = FlecheGauche, command=partial(self.TournerMoteur, "000500"))
        boutonTournerMoteurSens1.grid(row=2,column=1)

        
        boutonTournerMoteurSens2 = Button(MiniFrameBoutons, image =FlecheDroite, command=partial(self.TournerMoteur, "001500"))
        boutonTournerMoteurSens2.grid(row=2,column=3)

        boutonMonterMoteur = Button(MiniFrameBoutons, image=FlecheHaut, command=partial(self.TournerMoteur, "H+500"))
        boutonMonterMoteur.grid(row=1,column=2)

        boutonDescendreMoteur = Button(MiniFrameBoutons, image=FlecheBas, command=partial(self.TournerMoteur, "H-500"))
        boutonDescendreMoteur.grid(row=2,column=2)
        
        MiniFrameBoutons.grid(row=5,column=1, columnspan=4)
        FrameArduino.grid(row=2,column=1,sticky="nsew")


        #Pour afficher le menu
        self.menu(fenetre)

        
        fenetre.mainloop()
        self.statut = 0
        
    def linkBlender(self,lien):
        filename = askopenfilename(title="Lien vers blender",filetypes=[('exe files','.exe'),('all files','.*')])

        if(filename != "" ):
            try:
                config = open("SAVES/config.txt", "r")
                configComplete = config.read()
                config.close()
                                  
                config = open("SAVES/config.txt", "r")
                ligne = config.readline()
                ligne = config.readline()
                ligne = config.readline()
                ligne = config.readline()
                valeurOld = ligne
                valeurOld = valeurOld.replace("blender: ", "")
                config.close()
                              
                newConfig = configComplete.replace("blender: "+valeurOld,"blender: "+filename)
                                  
                config = open("SAVES/config.txt", "w")
                config.write(newConfig)
                lien.set(filename)
                config.close()
            except FileNotFoundError:
                ecrire("FICHIER CONFIG NON TROUVE", color="error")

        else:
            ecrire("Valeur entrée incorrecte." , color="error")

        
            
    def validerCamera(self,EntryCamera, ValeurCamera,intEntryCamera):
        valeur = EntryCamera.get()
        try:
            if(int(valeur)<0):
                ecrire("Valeur entrée incorrecte." , color="error")
            else:
                try:
                    config = open("SAVES/config.txt", "r")
                    configComplete = config.read()
                    config.close()
                                      
                    config = open("SAVES/config.txt", "r")
                    ligne = config.readline()
                    ligne = config.readline()
                    valeurOld = ligne
                    valeurOld = valeurOld.replace("camera: ", "")
                    config.close()
                                  
                    newConfig = configComplete.replace("camera: "+valeurOld,"camera: "+valeur+"\n")
                                      
                    config = open("SAVES/config.txt", "w")
                    config.write(newConfig)
                    ValeurCamera.configure(text=valeur)
                    intEntryCamera.set("")
                    config.close()
                except FileNotFoundError:
                    ecrire("FICHIER CONFIG NON TROUVE", color="error")
        except ValueError:
            ecrire("Valeur entrée incorrecte." , color="error")

    def validerUsb(self,EntryUsb, ValeurUsb,intEntryUsb):
        valeur = EntryUsb.get()
        if(valeur != "" ):
            try:
                config = open("SAVES/config.txt", "r")
                configComplete = config.read()
                config.close()
                                  
                config = open("SAVES/config.txt", "r")
                ligne = config.readline()
                ligne = config.readline()
                ligne = config.readline()
                valeurOld = ligne
                valeurOld = valeurOld.replace("usb: ", "")
                config.close()
                              
                newConfig = configComplete.replace("usb: "+valeurOld,"usb: "+valeur+"\n")
                                  
                config = open("SAVES/config.txt", "w")
                config.write(newConfig)
                ValeurUsb.configure(text=valeur)
                intEntryUsb.set("")
                config.close()
            except FileNotFoundError:
                ecrire("FICHIER CONFIG NON TROUVE", color="error")

        else:
            ecrire("Valeur entrée incorrecte." , color="error")

    #fonction qui transmet l'information au main une requette de changement de vue
    def vue(self, number):
        self.IndexVue = number

    #fonction qui transmet l'information au main que un des boutons tourner moteur à été cliqué
    def TournerMoteur(self, number):
        self.VariableMoteur = number

    #fonction qui transmet l'information au main que le bouton visualiser à été cliqué
    def Visualiser(self, number):
        self.indiceVisualiser = number

    #fonction qui test si l'arduino / le laser est branché
    def AttemptSerial(self):
        com = getUSB()
        if(com == "ERROR01"):
            ecrire("Gros probleme dans la config: \"usb\" n'a pas été trouvé !", color="error")
        else:
            try:
                varg.serial = serial.Serial(com,timeout=2)
                ecrire("Connection établie !",color="retour")
                self.boutonConnecter.configure(bg="#1a600a")
            except serial.SerialException :
                ecrire("Erreur de connection :"+com,color="error")
                self.boutonConnecter.configure(bg="#7f1a08")

    """
    Fonction qui crée le menu de la fenetre
    """
    def menu(self,fenetre):
        fenetre.resizable(False, False)
        fenetre.title('Scanner 3D programme')

        #Declaration du menu(en Haut)
        menu = Menu(fenetre, bg="red")

        #Menu Fichier
        menuFichier = Menu(menu, tearoff=0, bg="#EBEBEB")
        menuFichier.add_command(label="Nouveau...", command= partial(nouveau))
        menuFichier.add_command(label="Ouvrir...", command= partial(ouvrir))
        menuFichier.add_separator()
        menuFichier.add_command(label="Quitter", command= fenetre.destroy)

        menu.add_cascade(label="Fichier", menu=menuFichier)


        #Calibration
        menuCalibration = Menu(menu, tearoff=0, bg="#EBEBEB")
        menuCalibration.add_command(label="Calibration", command= partial(calibrationFenetre,fenetre))

        menu.add_cascade(label="Calibration", menu=menuCalibration)

        #Menu A propos
        menuApropos = Menu(menu, tearoff=0, bg="#EBEBEB")
        menuApropos.add_command(label="Informations", command= partial(informations,fenetre))

        menu.add_cascade(label="A propos", menu=menuApropos)


        #Menu Scanner
        menuScanner = Menu(menu, tearoff=0, bg="#EBEBEB")
        menuScanner.add_command(label="Scanner", command=partial(lancerScan,fenetre))

        menu.add_cascade(label="Scanner", menu=menuScanner)


        #Visualiser
        menuVisualisation = Menu(menu, tearoff=0, bg="#EBEBEB")
        menuVisualisation.add_command(label="Visualiser", command=partial(self.Visualiser, 1))

        menu.add_cascade(label="Visualisation", menu=menuVisualisation)

        fenetre.config(menu = menu)


def lancerScan(fenetre):
    fen = FenetreScan(fenetre)
