import numpy as np
import matplotlib.pyplot as plt
import itertools
from PyAstronomy import pyasl
#Opening the files and Converting the contents to an arrays
cosmicray = open('/home/austin/docs/cp/AVD/sunproject/climax.tab')
sunspot = open('/home/austin/docs/cp/AVD/sunproject/SSmeans.txt')


CA=cosmicray.read().split()
CA=CA[20:-80]
SS=sunspot.read().split()
SS=SS[20:-1]

CA=np.array(CA)
CA.shape=(51,14)
CA=CA.astype(int)
SS=np.array(SS)
SS=SS.astype(float)
SS.shape=(51,13)

#Filtering out the first and last coulmns as they are years&the mean
years=CA[:,[0]]
years=years.astype(str)
years=years.tolist()
CA=CA[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
CA=CA.tolist()
SS=SS[:,[1,2,3,4,5,6,7,8,9,10,11,12]]
SS=SS.tolist()
#Un-nesting or flattening the list
years=list(itertools.chain(*years))
CA=list(itertools.chain(*CA))
SS=list(itertools.chain(*SS))
#Converting the list back into an array
CA=np.array(CA)
SS=np.array(SS)
#Beginning to plot
x=np.arange(0,612,1)
CAn=CA
SSn=SS
#Using the PyAstronomy package to creating moving averages
#to smoooth the data
CAf=pyasl.smooth(CA,11,'flat')
CAh=pyasl.smooth(CA,11,'hamming')
SSf=pyasl.smooth(SS,11,'flat')
SSh=pyasl.smooth(SS,11,'hamming')



fig, (axs1,axs2) = plt.subplots(2,1,sharex=True)
axs1.set_title('Monthly Cosmic Ray Activity')
axs2.set_title('Monthly mean Sun-Spots')
axs1.plot(x, CAn,color='grey',alpha=0.3)
axs1.plot(x,CAf,color='red',alpha=0.4)
axs1.plot(x,CAh,color='blue',alpha=0.4)
axs2.plot(x, SSn,color='grey',alpha=0.3)
axs2.plot(x, SSf,color='red',alpha=0.4)
axs2.plot(x, SSh,color='blue',alpha=0.4)
fig.canvas.draw()
labels = [item.get_text() for item in axs2.get_xticklabels()]
labels[1] = '1953'
labels[2]='1966'
labels[3]='1991'
labels[4]='2003'
labels[5]='1993'
labels[6]='2003'
labels=labels[0:-1]
axs2.xaxis.set_major_locator(plt.MaxNLocator(11))
print(labels)
axs2.set_xticklabels(labels)

plt.show()
