def ArraySeries(n):
    d= [0]*n
    c=1
    a=[]
    for i in range(len(d)-1,-1,-1):
        d[i]=c
        c+=1
        for j in d:
            a.append(j)
    print(a)

ArraySeries(4)
