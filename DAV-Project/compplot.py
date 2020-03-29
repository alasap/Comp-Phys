#Created by Austin Hall
#March 2020
#Computational Physics Sun-Project Plot
import numpy as np
import matplotlib.pyplot as plt
import itertools
import seaborn as sns
sns.set()

#Opening the files and Converting the contents to an arrays
cosmicray = open('/home/austin/docs/cp/DAV-Project/climax.tab')
sunspot = open('/home/austin/docs/cp/DAV-Project/SSmeans.txt')


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
    elif i>=1 and i<4:
        avg=(CAn[i-1]+CAn[i]+CAn[i+1])/3
        CAma=np.append(CAma,[avg])
        i=i+1
    elif i>606 and i<611:
        avg=(CAn[i-1]+CAn[i]+CAn[i+1])/3
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
    elif i>=1 and i<4:
        avgS=(SSn[i-1]+SSn[i]+SSn[i+1])/3
        SSma=np.append(SSma,[avgS])
        i=i+1
    elif i>606 and i<611:
        avgS=(SSn[i-1]+SSn[i]+SSn[i+1])/3
        SSma=np.append(SSma,[avgS])
        i=i+1
    else:
        SSma=np.append(SSma,SSn[i])
        i=i+1
#Finding the Max's and Min's in local regions of each data set to 
#quanitatively establish a connection

    #Max's and Min's of the Cosmic Ray Data
crmax1=(np.argmax(CAma[0:60]))
crmax2=(np.argmax(CAma[100:200]))+100
crmax3=(np.argmax(CAma[200:300]))+200
crmax4=(np.argmax(CAma[350:450]))+350
crmax5=(np.argmax(CAma[500:612]))+500
crmin1=(np.argmin(CAma[0:100]))
crmin2=(np.argmin(CAma[150:250]))+150
crmin3=(np.argmin(CAma[300:400]))+300
crmin4=(np.argmin(CAma[400:500]))+400
crmin5=(np.argmin(CAma[500:612]))+500

crmaxmin=np.empty((0,10))
crmaxmin=np.append(crmaxmin,[crmax1,crmin1,crmax2,crmin2,crmax3,crmin3,crmax4,crmin4,crmax5,crmin5])
print(crmaxmin)
    #Max's and Min's of the Sun-Spot Data
ssmax1=(np.argmax(SSma[0:100]))
ssmax2=(np.argmax(SSma[150:250]))+150
ssmax3=(np.argmax(SSma[275:375]))+275
ssmax4=(np.argmax(SSma[400:500]))+400
ssmax5=(np.argmax(SSma[525:612]))+525
ssmin1=(np.argmin(SSma[0:75]))
ssmin2=(np.argmin(SSma[100:200]))+100
ssmin3=(np.argmin(SSma[200:300]))+200
ssmin4=(np.argmin(SSma[350:450]))+350
ssmin5=(np.argmin(SSma[500:612]))+500

ssmaxmin=np.empty((0,10))
ssmaxmin=np.append(ssmaxmin,[ssmin1,ssmax1,ssmin2,ssmax2,ssmin3,ssmax3,ssmin4,ssmax4,ssmin5,ssmax5])
print(ssmaxmin)
#Setting up the two plots
fig, (axs1,axs2) = plt.subplots(2,1,sharex=True)
axs1.set_title('Cosmic-Ray Count',fontsize=15)
axs2.set_title('Sun-Spot Count',fontsize=15)
axs1.plot(x, CAn,color='grey',alpha=0.9,linewidth=0.7,label='NOAA Data-Sets')
axs1.plot(x,CAma,color='blue',alpha=1,linewidth=0.9,label='Moving Average')
axs2.plot(x, SSn,color='grey',alpha=0.9,linewidth=0.7)
axs2.plot(x, SSma,color='blue',alpha=1,linewidth=0.9)

#Plotting the Max and Min points as well

    #For the Cosmic-Ray Data
axs1.plot(crmax1, CAma[crmax1],'.',color='black',alpha=1,markersize=5)
axs1.plot(crmax2, CAma[crmax2],'.',color='black',alpha=1,markersize=5)
axs1.plot(crmax3, CAma[crmax3],'.',color='black',alpha=1,markersize=5)
axs1.plot(crmax4, CAma[crmax4],'.',color='black',alpha=1,markersize=5)
axs1.plot(crmax5, CAma[crmax5],'.',color='black',alpha=1,markersize=5)
axs1.plot(crmin1, CAma[crmin1],'.',color='r',alpha=1,markersize=5)
axs1.plot(crmin2, CAma[crmin2],'.',color='r',alpha=1,markersize=5)
axs1.plot(crmin3, CAma[crmin3],'.',color='r',alpha=1,markersize=5)
axs1.plot(crmin4, CAma[crmin4],'.',color='r',alpha=1,markersize=5)
axs1.plot(crmin5, CAma[crmin5],'.',color='r',alpha=1,markersize=5)

    #For the Sun-Spot Data
axs2.plot(ssmin1, SSma[ssmin1],'.',color='black',alpha=1,markersize=5)
axs2.plot(ssmin2, SSma[ssmin2],'.',color='black',alpha=1,markersize=5)
axs2.plot(ssmin3, SSma[ssmin3],'.',color='black',alpha=1,markersize=5)
axs2.plot(ssmin4, SSma[ssmin4],'.',color='black',alpha=1,markersize=5)
axs2.plot(ssmin5, SSma[ssmin5],'.',color='black',alpha=1,markersize=5)
axs2.plot(ssmax1, SSma[ssmax1],'.',color='r',alpha=1,markersize=5)
axs2.plot(ssmax2, SSma[ssmax2],'.',color='r',alpha=1,markersize=5)
axs2.plot(ssmax3, SSma[ssmax3],'.',color='r',alpha=1,markersize=5)
axs2.plot(ssmax4, SSma[ssmax4],'.',color='r',alpha=1,markersize=5)
axs2.plot(ssmax5, SSma[ssmax5],'.',color='r',alpha=1,markersize=5)
    
#Setting the x-axis label in ten year intervals
labels=['1953','1963','1973','1983','1993','2003']
ticks=np.arange(1,613,122)
axs2.set_xticks(ticks)
axs2.set_xticklabels(labels)
axs2.set_xlim([-5,620])
axs2.set_xlabel('Years',fontsize=15)
axs2.set_ylabel('$R_z = k(10g + s)$')
axs1.set_ylabel('Counts per Hour')
axs1.tick_params(labelsize=8)
axs1.legend(fontsize=8,loc='lower left')
#plt.show()

x1=np.linspace(0,10,10)
#plt.plot(x1,crmaxmin,'1',color='orange')
#plt.plot(x1,ssmaxmin,'.',color='b',alpha=0.50)
#plt.show()

plt.savefig('plot.png',dpi=1000)
