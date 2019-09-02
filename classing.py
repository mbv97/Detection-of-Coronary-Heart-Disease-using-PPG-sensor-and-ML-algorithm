def classify(path):
        file1=open(path)
        lst1=[]
        while(True):
                str=file1.readline();
                if(len(str)==0):
                        break;
                lst=str.split(",")
                if(len(lst)>2 and flag==1):
                        lst1.append(lst[3])
		
        for i in lst1:
                if i>= 414 and i<415:
                        return(1);
                else:
                        return(0);
