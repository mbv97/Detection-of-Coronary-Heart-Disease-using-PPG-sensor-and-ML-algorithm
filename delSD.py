import numpy as np
def delSD(a,p_max, s_max):
    diff=[]
    l1=len(p_max)
    l2=len(s_max)
    l1=min(l1,l2)
    avg=[0,0]
    avg[0]=np.mean(a[p_max])/np.mean(a[s_max])
    avg[1]=(np.mean(a[p_max])-np.mean(a[s_max]))/np.mean(a[p_max])

    return (avg)
