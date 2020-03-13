#B1:using a mask to pull out array elements less than 5 or
#greater-than/equal-to 7.
import numpy as np
a=np.array([0,1,2,3,4,5,6,7,8,9,10])
m1=a<5
m2=(a>=7)
print(a[m1],a[m2])

#B2:Indexing a fluid array using a string matching column names
fluid=np.dtype([('x',int),
               ('y',np.int64),
               ('rho','f8')])
print(fluid[['x','y','rho']])

#B3:plotting sin using numpy and pylab
import pylab
x=np.linspace(0,10,1000)
y=np.sin(x)
pylab.plot(x,y)
pylab.show()

#B4:Plot a 2d density map of wave interference
from pylab import imshow,gray,show
wavelength=5.0
k=2*np.pi/wavelength
amp=1.0
sep=25.0
side=100.0
points=500
spacing=side/points

x1=side/2+sep/2
y1=side/2
x2=side/2-sep/2
y2=side/2

xi=np.empty([points,points],float)
for i in range(points):
    y=spacing*i
    for j in range(points):
        x=spacing*j
        r1=np.sqrt((x-x1)**2+(y-y1)**2)
        r2=np.sqrt((x-x2)**2+(y-y2)**2)
        xi[i,j]=amp*np.sin(k*r1)+amp*np.sin(k*r2)
imshow(xi,origin='lower',extent=[0,side,0,side])
gray()
show()
