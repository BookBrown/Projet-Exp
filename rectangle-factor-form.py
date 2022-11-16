import matplotlib.pyplot as plt
import numpy as np


def I(qx,qy,a,b):
    return((4*(np.sin(a*qx/2)*np.sin(b*qy/2))/(qx*qy))**2)
 
qx=np.linspace(-10,10,1000)
qy=np.linspace(-10,10,1000)

a=3
b=5
      
qqx,qqy=np.meshgrid(qx,qy)
plt.pcolormesh(qx,qy,I(qqx,qqy,a,b))
plt.colorbar()
plt.show()

