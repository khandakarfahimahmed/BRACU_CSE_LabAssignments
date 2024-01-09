def Repitition(a):
    a1=[]
    d = []
    c = 0
    s = "False"
    for b in a:
        if b not in a1:
            a1.append(b)
    for i in range(0,len(a1)):
        for j in a:
            if a1[i]==j:
                c+=1
        d.append(c)
        c=0
    for k in range(0,len(d)):
        for p in range(k+1,len(d)):
            if d[k]>1 and d[p]>1:
                if d[k]==d[p]:
                    s="True"
                    break
    print(s)

a = [3,4,6,3,4,7,4,6,8,6,6]
Repitition(a)
