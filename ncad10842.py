import wfdb
import delSD
from scipy import signal
import matplotlib.pyplot as plt
import os
from scipy.signal import butter, lfilter, filtfilt
import sri_31
import numpy as np

def butter_bandpass(data, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    y=y[::-1]
    y=y+600
    return y

path='/home/reetu/www.physionet.org/physiobank/database/mimic2wdb/matched/s10842/'
lst=[]
for filename in os.listdir(path):
    lst.append(filename)
lst.sort()
for i in range(1,len(lst),2):
    str=lst[i]
    sig,fld=wfdb.srdsamp(path+(str[0:len(str)-4]))
    rec=wfdb.rdsamp(path+(str[0:len(str)-4]))	
    #print(sig)
    #print(fld)


    sig_name=fld['signame']
    flg=1
    for k in range(len(sig_name)):
        if sig_name[k]== 'PLETH':
            flg=0;
            print(k)
            break;
    if flg==0:
        sz=list(sig.shape)
        print(sz)
        print(str[0:len(str)-4])
        if(sz[0]<15000):
            print('error')
            continue
        #k1=(sz[0]-7500)
        #k1=k1//2
        k1=5000
        a=rec.adc()[:,k]
        #print(k1, k1+7500)
        a=a[k1:k1+7500]
        plt.plot(a)
        plt.title(str[0:len(str)-4])
        plt.show()
        y=butter_bandpass(a, 0.5, 3, 125, 2)
        plt.plot(y)
        plt.title('Butterworth')
        plt.show()

        p_max,s_max=sri_31.pk_max(y)


        plt.plot(y[p_max]*(10**-3), 'b*-')
        plt.ylim(0,1)
        plt.show()
        
        fr,Pxx_den=signal.welch(y[p_max], 2)
        plt.plot(fr, Pxx_den)
        plt.title('PSD')
        plt.show()

        print('Mean =', delSD.delSD(y,p_max, s_max))
    else:
        print('error')

