def removeAll(source,size,element):
    d = []
    for i in range(0,size):
        if source[i]==element:
            source[i]=0
        else:
            d.append(source[i])
            source[i]=0
    for j in range(0,len(d)):
        source[j]=d[j]
    print(source)


source = [10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
