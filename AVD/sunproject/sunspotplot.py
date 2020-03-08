import numpy as np
import itertools
import matplotlib.pyplot as plt

f = open('/home/austin/Desktop/SSmeans.txt')
array=f.read().split()
array=array[20:-1]
len=len(array)
print(len)
array=np.array(array)

array=array.astype(float)
array.shape=(51,13)
array=array[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
array=array.tolist()
#Un-nesting or flattening the list
arrayflat=list(itertools.chain(*array))
#Converting the list back into an array
array=np.array(arrayflat)

print(array)
x=np.arange(0,612,1)
plt.plot(x,array)
plt.show()
