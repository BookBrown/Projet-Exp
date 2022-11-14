import numpy as np
import matplotlib.pyplot as plt


def I(qx,qy,a,b):
    return((4*(np.sin(a*qx/2)*np.sin(b*qy/2))/(qx*qy))**2)
 
qx=np.linspace(-10,10,1000)
qy=np.linspace(-10,10,1000)

a=5
b=5
      
qqx,qqy=np.meshgrid(qx,qy)
plt.pcolormesh(qx,qy,I(qqx,qqy,a,b))
plt.colorbar()
plt.show()