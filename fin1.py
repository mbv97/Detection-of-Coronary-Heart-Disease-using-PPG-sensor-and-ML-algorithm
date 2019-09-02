import wfdb
import delSD
from scipy import signal
import matplotlib.pyplot as plt
import os
from scipy.signal import butter, lfilter, filtfilt
import sri_31
import classing
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

path='/media/reetu/MYDISC/Proj final'
lst=[]
for filename in os.listdir(path):
    lst.append(filename)
lst.sort()

for i in range(0,len(lst)):
    path2=path+'/'+lst[i]
    lst2=[]
    for filename in os.listdir(path2):
        lst2.append(filename)
    lst2.sort()
    c=lst2.pop()
    cad=classing.classify(path2+'/'+c)
    print(cad)
    input()
    
