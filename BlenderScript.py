import bpy
import numpy as np
import math
import sys
import os

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )
    #print(sys.path)

import fonctionsFichierProvisoire as fichierProvisoire
import fonctionsFichier as fichier

# this next part forces a reload in case you edit the source after you first start the blender session
import imp
imp.reload(fichierProvisoire)
imp.reload(fichier)

def createMesh(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = True
    # Link object to scene
    bpy.context.scene.objects.link(ob)
 
    # Create mesh from given verts, edges, faces. Either edges or
    # faces should be [], or you ask for problems
    me.from_pydata(verts, edges, faces)
 
    # Update mesh with new data
    me.update(calc_edges=True)
    return ob
 
def run(origin,verts,nom):
    (x,y,z) = (0.707107, 0.258819, 0.965926)


    ob2 = createMesh(nom.replace("\n",""), origin, verts, [] , [])
 
    # Move second object out of the way

    return
def decrypt(path):
    file = open(path,"r")
    nom = fichier.getNom(file)
    date = fichier.getDate(file)
    precision = fichier.getPrecision(file)
    distance = float(fichier.getDistance(file))
    angle = float(fichier.getAngle(file))
    
    title,lineDetect = file.read().split("!")
    
    ListHeight = lineDetect.split("\n")
    
    n = 0
    for line in ListHeight :
        if line == ListHeight[0]:
            coordPx = np.array([line.split(":")] )
            b = n
            n = np.size(coordPx)
            
            
        else:
            try:
                coordPx = np.append(coordPx,  [line.split(":")] , axis=0 )
                b = n
                n = np.size(coordPx)
                
            except ValueError:
                pass
    return title,coordPx,angle,distance,nom
def vertGenerator(coord,A,E) : 

    verts = []
    B = 63.1
    Bp = 49.5
    d = 640
    dp = 480
    
    for step in range(coord.shape[0]) :
                
        for H in range(coord.shape[1]) :
        
            if(coord[step,H]!="" and coord[step,H]!="0.0"):
                X=0
                Y=0


               
                x = float(coord[step,H])
                D = 180-(180-B)/2-(B*x)/d
                Dp = 180-(180-Bp)/2-(Bp*H)/dp

                t = (-3*E)/(1+math.tan(math.radians(D))*math.tan(math.radians(A)))

                
                X = (t+3*E)/(math.tan(math.radians(D)))


                J = (360/coord.shape[0])*step
                R = (abs(X))/math.sin(math.radians(A))
                C = (180-J) /2
                
                K = 2*R * math.cos( math.radians(C) )
                G = 180-C-90+A

                
                X = X#+ K*math.cos(math.radians(G))
                Y = t# + K*math.sin(math.radians(G))
                Z = (t+3*E)/math.tan(math.radians(Dp))
                
                verts.append( ( X*0.1 , Y*0.1, -Z*0.1))

    return verts

 
if __name__ == "__main__":
    
    title,coord,angle,distance,nom = decrypt(fichierProvisoire.link().lien)
    
    verts = vertGenerator(coord,angle,distance)

    run((0,0,0),verts,nom)
    #print(str(ListHeight))
    #print(title)
    #Debug = open("C:\\Users\\user\\Desktop\\LeTpeVersionActuelVideo\\blenderrun\\Debug.txt","w")
    #fichierProvisoire.link().lien
    #Debug.write(np.array2string(coord, precision=2, separator=','))
    #print(coord.shape)
