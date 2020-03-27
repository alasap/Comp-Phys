#Created by Austin Hall
#March 2020
#Computational Physics Sun-Project Plot
import numpy as np
import matplotlib.pyplot as plt
import itertools
from PyAstronomy import pyasl
#import seaborn as sns
#sns.set()

#Opening the files and Converting the contents to an arrays
cosmicray = open('/home/alasap/docs/cp/sunproject/climax.tab')
sunspot = open('/home/alasap/docs/cp/sunproject/SSmeans.txt')


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
#Multiplying the Cosmic Ray data to determine the hourly counting rate
CA=CA*100
#Beginning to plot
x=np.arange(0,612,1)
CAn=CA
SSn=SS
#trying to create my own moving average
CAma=np.empty((0,612))
i=0
while i<=len(CAn)-1:
    if i>=4 and i<=606:
        avg=(CAn[i-5]+CAn[i-4]+CAn[i-3]+CAn[i-2]+CAn[i-1]+CAn[i]+CAn[i+1]+CAn[i+2]+CAn[i+3]+CAn[i+4]+CAn[i+5])/11
        CAma=np.append(CAma,[avg])
        i=i+1
    else:
        CAma=np.append(CAma,CAn[i])
        i=i+1


SSma=np.empty((0,612))
i=0
while i<=len(SSn)-1:
    if i>=4 and i<=606:
        avgS=(SSn[i-5]+SSn[i-4]+SSn[i-3]+SSn[i-2]+SSn[i-1]+SSn[i]+SSn[i+1]+SSn[i+2]+SSn[i+3]+SSn[i+4]+SSn[i+5])/11
        SSma=np.append(SSma,[avgS])
        i=i+1
    else:
        SSma=np.append(SSma,SSn[i])
        i=i+1




fig, (axs1,axs2) = plt.subplots(2,1,sharex=True)
axs1.set_title('Cosmic Ray Activity',fontsize=20)
axs2.set_title('Sun-Spot Count',fontsize=20)
axs1.plot(x, CAn,color='grey',alpha=0.3,label='Given Data')
axs1.plot(x,CAma,color='blue',alpha=0.4,label='Hamming Smoothing')
axs2.plot(x, SSn,color='grey',alpha=0.3)
axs2.plot(x, SSma,color='blue',alpha=0.4)
labels=['1953','1963','1973','1983','1993','2003']

ticks=np.arange(1,613,122)
axs2.set_xticks(ticks)
axs2.set_xticklabels(labels)
axs2.set_xlim([-5,620])
axs2.set_xlabel('Years',fontsize=15)
axs2.set_ylabel('$R_z = k(10g + s)$')
axs1.set_ylabel('Counts per Hour')
axs1.legend(fontsize=8,loc='lower left')

plt.show()
#plt.savefig('plot.jpg',dpi=2500,figsize=(6,4))
