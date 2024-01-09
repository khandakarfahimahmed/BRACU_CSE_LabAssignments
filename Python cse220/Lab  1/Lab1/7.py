def MaxBunchCount(a):
    c = 0
    max = 0
    d=[]
    rec=a[0]
    for i in a:

        if rec==i:
            c+=1
        else:
            d.append(c)
            rec=i
            c=1
        if i==a[-1]:
            d.append(c)
    max=d[0]
    for i in range(0,len(d)):
        if max>d[i]:
            pass
        else:
            max=d[i]
    print(max)
a= [1,2,2,3,4,4,4]
MaxBunchCount(a)
