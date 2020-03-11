import numpy as np
import matplotlib.pyplot as plt
import itertools
from PyAstronomy import pyasl
#Opening the file and Converting the contents to an array
f = open('/home/austin/docs/cp/AVD/sunproject/climax.tab')
array=f.read().split()
array=array[20:-80]

A=np.array(array)
A.shape=(51,14)
A=A.astype(int)
#Filtering out the first and last coulmns as they are years&the mean
A=A[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
A=A.tolist()
#Un-nesting or flattening the list
Aflat=list(itertools.chain(*A))
#Converting the list back into an array
Aflat=np.array(Aflat)

#Beginning to plot
x=np.arange(0,612,1)
y=Aflat
#Using the PyAstronomy package to creating moving averages
#to smoooth the data
yflat=pyasl.smooth(Aflat,11,'flat')
yhamming=pyasl.smooth(Aflat,11,'hamming')
plt.plot(x,y,color='gray',alpha=0.3)
plt.plot(x,yflat,color='r',alpha=0.4)
plt.plot(x,yhamming,color='blue',alpha=0.4)
plt.show()
