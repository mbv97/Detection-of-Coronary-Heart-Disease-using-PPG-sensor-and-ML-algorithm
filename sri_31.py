import numpy as np
import matplotlib.pyplot as plt
def pk_max(a):
        start=0
        ad=np.diff(a)
        ad=np.insert(ad,0,start)
        zc = (np.where(np.diff(np.sign(ad)))[0])+1
        for i in range(len(zc)-1):
                if(((zc[i]-zc[i-1])<=1)):
                        zc[i]=0
        zc=zc[np.nonzero(zc)]
        min_g=[]
        max_g=[]
        for i in zc:
                if(ad[i+1]>0):
                        min_g.append(i)
                elif(ad[i+1]<0):
                        max_g.append(i)
        #print(min_g)
        #print(max_g)
        p_max=[max_g[0]]
        s_max=[]
        prev=1
        if min_g[0]<max_g[0]:
            min_g=min_g[1:]
        for i in range(len(min_g)-1):
            mx=max_g[i]
            mn=min_g[i]
            mx1=max_g[i+1]
            if((a[mn]>=a[mx]*0.5)or(a[mx1]<=0.5*a[mx]))and prev==1 and a[mx1]<a[mx]:
                s_max.append(mx1)
                prev=0
            else:
                p_max.append(mx1)
                prev=1
        plt.plot(a)
        plt.plot(p_max,a[p_max],'b*')
        plt.plot(s_max,a[s_max],'r*')
        plt.show()
        return (p_max,s_max)
