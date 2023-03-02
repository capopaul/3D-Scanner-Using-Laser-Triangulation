import cv2
import sys
import numpy as np
from PIL import Image
from PIL import ImageTk

import VariableGlobal as varg
import time


def nothing(x):
    pass


def scan(mat): #fonction pour scanner le threshold
    a=mat.shape[0]
    b=mat.shape[1]
    #print(str(a)+" "+str(b))
    retour=np.zeros(a)
    
    y=0
    while y < (a-1):

        x=0

        temparr=np.array([0])
        
        while x < (b-1) :
            if mat[y,x]>0 :
                temparr=np.append(temparr,x)              
            
            
            x+=1

        temparr=np.delete(temparr,0)
        if temparr.size >0:
            retour[y]=np.mean(temparr)

        
        y+=1

    
    return retour

def viscan(mask,arr): #fonction pour visualiser l'array du scan
    
    maskblack=np.zeros_like(mask)
     
    y=0
    while y<arr.size:
        maskblack.itemset( ( y , int( arr[y] )  ) , 255 )
        y+=1
        
        
    return maskblack

def threshold(img,hl,sl,vl,hu,su,vu): #fonction pour obtenir le threshold entre les valeur HSV- et HSV+ d'une image (en noir et blanc)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([hl,sl,vl])
    upper_blue = np.array([hu,su,vu])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    return mask

def brightness(img,value):
    imgret=cv2.add(img , np.ones_like(img)+value)
    return imgret

def convertTk(frame):
    if(len(frame.shape) == 3):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    image = ImageTk.PhotoImage(frame)
    return image

#un tour 2048 pas

def Scanning(cap,Heights,Precision,hl,sl,vl,hu,su,vu):
    ret,frame =  cap.read()
    fond = cv2.imread("SAVES\imageFond.jpg")
    Return = "!"
    
    Step = int(2048/Precision)
    for H in range(Heights):

        for x in range(Step):

            ret,frame =  cap.read()
            
            ThresholdT = threshold(frame,hl,sl,vl,hu,su,vu)
            Line=scan(ThresholdT)

            for v in range(len(Line)):

                Return += str(Line[v])+":"

            cv2.imshow("debug", viscan(ThresholdT,Line) )

            k = cv2.waitKey(1) & 0xFF
            
            varg.serial.write(str("001"+str(Precision)).encode('utf-8'))
            Return += "\n"

            time.sleep(0.4)

            
    cv2.destroyAllWindows()
    return Return






































##np.set_printoptions(threshold=np.inf)

### imgread
##img = cv2.imread('laser.jpg')
##
##
##
##cv2.imshow('img', img)
##
##
##
##
##cv2.namedWindow('image')
##
### création des trackbars
##cv2.createTrackbar('H-','image',0,179,nothing)
##cv2.createTrackbar('S-','image',0,255,nothing)
##cv2.createTrackbar('V-','image',0,255,nothing)
##
##cv2.createTrackbar('H+','image',0,179,nothing)
##cv2.createTrackbar('S+','image',0,255,nothing)
##cv2.createTrackbar('V+','image',0,255,nothing)
##cv2.createTrackbar('brightness','image',0,100,nothing)
##
##
##
##
##while(1): #boucle principal
##
##
##    # avoir les position des trackbars
##    h = cv2.getTrackbarPos('H-','image')
##    s = cv2.getTrackbarPos('S-','image')
##    v = cv2.getTrackbarPos('V-','image')
##
##    hu = cv2.getTrackbarPos('H+','image')
##    su = cv2.getTrackbarPos('S+','image')
##    vu = cv2.getTrackbarPos('V+','image')
##    brg = cv2.getTrackbarPos('brightness','image')
##
##    img2= brightness(img,brg)
##    
##    cv2.imshow('img2', img2)
##    
##    mask = threshold(img2,h,s,v,hu,su,vu)  #threshold de l'image
##
##    res = cv2.bitwise_and(img2,img2, mask= mask) # image soustraite du threshold
##    
##    cv2.imshow('img3', mask) #affichage du threshold
##    
##    cv2.imshow('image',res) #affichage de la soustraction
##
##
##
##    k = cv2.waitKey(1) & 0xFF
##    if k == 27:
##
##        break
##        
##    if k == 13:
##        location = scan(mask) #array scan
##        
##        maskb=viscan(mask,location) #image scan
##
##        cv2.imshow('locat',maskb) # affichage image scan
##
##        hsvinf=str(h)+'\n'+str(s)+'\n'+str(v)+'\n'+str(hu)+'\n'+str(su)+'\n'+str(vu)+'\n \n'
##
##        f = open('filetest.txt','w')
##        f.write(hsvinf+str(location))
##        f.close()
##        
##
##
##
##    
##cv2.destroyAllWindows()










