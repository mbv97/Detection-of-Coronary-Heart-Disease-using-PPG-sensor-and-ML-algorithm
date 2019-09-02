import numpy as np
import matplotlib.pyplot as plt
def read_value():
    ppg=open('/home/reetu/data.txt','r')
    a=[]
    while True:
        val=ppg.readline()
        if len(val)==0:
            break;
        a.append(float(val))
    a=np.array(a)

    plt.plot(a)
    plt.show()
    return a

read_value()
