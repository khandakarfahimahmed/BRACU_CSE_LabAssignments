def Intersection(a,start,size,b,start1,size1):
    d = []
    d1=[]
    c = 0
    common = []
    for i in range(start,len(a)):
        if a[i]==0:
            break
        d.append(a[i])
        c+=1
    diff = size-c
    if diff >0:
        for j in range(0,diff):
            d.append(a[j])
    c=0
    for i in range(start1,len(b)):
        if b[i]==0:
            break
        d1.append(b[i])
        c+=1
    diff = size1-c
    if diff >0:
        for j in range(0,diff):
            d1.append(b[j])
    for i in d:
        for j in d1:
            if i==j:
                common.append(i)
    print(common)
a = [40,50,0,0,0,10,20,30]
b = [10,20,5,0,0,0,0,0,5,40,15,25]
Intersection(a,5,5,b,8,7)
