import numpy as np
import matplotlib.pyplot as plt


def PolMid(Som):  #prend en entrée la liste des sommets
    N=len(Som)-1
    PosAr=[] #milieu des arêtes
    VecAr=[] #vecteurs directeurs des arêtes
    
    for i in range(1,N+1):
        r=0.5*(Som[i]+Som[i-1])
        e=0.5*(Som[i]-Som[i-1])
        PosAr.append(r)
        VecAr.append(e)
        
    return(np.array(PosAr),np.array(VecAr))

def FormFactor(q,Som):
    N=len(Som)-1
    Pos,Vec=PolMid(Som) #on récupère les sommets, les milieux des arêtes et vecteurs directeurs
    qx,qy=q[0],q[1] #selon les directions x ou y
    c=0 #on suppose ici que c vaut 0 dans la formule de Wuttke
    s=0 #notre somme de termes pour calculer le facteur de forme d'après la formule de Wuttke.
    for i in range(N):
        ex,ey=Vec[i][0],Vec[i][1]
        rx,ry=Pos[i][0],Pos[i][1]
        
        s+=(qx*ey-qy*ex)*(np.sinc((qx*ex+qy*ey)/np.pi)*np.exp(1j*(qx*rx+qy*ry))-c)
        
    return(2*s/(1j*(qx*qx+qy*qy)))