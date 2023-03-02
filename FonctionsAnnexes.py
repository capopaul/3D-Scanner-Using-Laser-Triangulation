import VariableGlobal as varg
from tkinter import *
"""
Fonction ecrire qui print du texte dans la console de la fenetre tkinter
*tag = couleur attendu. tag = "red" "blue" ou "black"
"""
def ecrire(text,**tagg):   #fonction insert du text dans les logs

    varg.console.configure(state="normal")
    color = tagg.get('color', None)
    if(color == "retour"):
        varg.console.insert(END,">>> "+text+"\n","blue")
    elif(color == "error"):
        varg.console.insert(END,"[ERROR] "+text+"\n","red")
    else:
        varg.console.insert(END,text+"\n",color)
    varg.console.yview("scroll", 1000, "units")
    varg.console.configure(state="disabled")
