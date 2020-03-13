#C1:changing the shape of a numpy array
import numpy as np
array=np.array([1,2,3,4,5])
array=np.reshape(array,(5,1))
print(array)

#C2:print the data type of a numpy array
print(array.dtype)

#C3:addition of arrays
array=np.array([1,1,1])
array2=np.array([[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
array3=np.add(array,array2)
print(array3)

#C4:Pull out the fourth , last and second elements of a numpy array
a=np.array([0,1,2,3,4,5,6,7,8,9])
print(a[[3,-1,1]])

#C5: mask a numpy array
import numpy.ma as ma
array=ma.array(a,mask=[1,0,0,0,0,0,0,0,0,0])
print(array)
 #C6:creating a structured fluid type array
fluid=np.dtype([('x',int),
              ('y',np.int64),
              ('rho','f8')])
print(fluid)

#C7:use numpy to calculate the mean of an array
print(np.mean(array))

#C8:appending an array to another array
array2=np.array([10])
print(np.append(array,array2))

#C9&10:plotting with data from a file and adding axis labels
import matplotlib.pyplot as plt
x,y= np.loadtxt('/home/austin/docs/cp/AVD/plot.csv', delimiter=',', unpack=True)
plt.plot(x,y)
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.title('Sample Title\n(This was loaded from a data file)')
plt.show()
