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
        p_max=[]
        s_max=[]
        for i in range(len(max_g)):
                if(i<len(max_g)-1):
                        m=max_g[i+1]
                        n=max_g[i]
                        if(a[m]>a[n]):
                                s_max.append(n)
                        elif(a[n]>a[m]):
                                p_max.append(n)
                elif(i==len(max_g)-1):
                        m=max_g[i]
                        n=max_g[i-1]
                        if(a[m]>=a[n]):
                                p_max.append(m)
                        else:
                                s_max.append(m)
        return (p_max,s_max,max_g)
