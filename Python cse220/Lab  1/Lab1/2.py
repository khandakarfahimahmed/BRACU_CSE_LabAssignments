def rotateLeft(source,k):
    d = []
    t = 0
    for i in range(0,len(source)):
        t = i-k
        if t<0:
            d.append(source[i])
    for j in range(len(source)-1,-1,-1):
        if source[j] not in d:
            source[j-k]=source[j]
    t= len(source)
    for m in range(0,len(d)):

        source[(t-k)] = d[m]
        t+=1
    print(source)
source=[10,20,30,40,50,60]
rotateLeft(source,3)
