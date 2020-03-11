import numpy as np
import itertools
import matplotlib.pyplot as plt
from PyAstronomy import pyasl

f = open('/home/austin/docs/cp/AVD/sunproject/SSmeans.txt')
array=f.read().split()
array=array[20:-1]
array=np.array(array)

array=array.astype(float)
array.shape=(51,13)
array=array[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
array=array.tolist()
#Un-nesting or flattening the list
arrayflat=list(itertools.chain(*array))
#Converting the list back into an array
array=np.array(arrayflat)

yflat=pyasl.smooth(array,11,'flat')
yhamming=pyasl.smooth(array,11,'hamming')

x=np.arange(0,612,1)
plt.plot(x,array,color='gray',alpha=0.3)
plt.plot(x,yflat,color='red',alpha=0.4)
plt.plot(x,yhamming,color='blue',alpha=0.4)

plt.show()
