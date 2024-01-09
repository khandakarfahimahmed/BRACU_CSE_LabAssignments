def palindrome(a,start,size):
    d = []
    c = 0
    s=""
    for i in range(start,len(a)):
        if a[i]==0:
            break
        d.append(a[i])
        c+=1
    diff = size-c
    if diff >0:
        for j in range(0,diff):
            d.append(a[j])
    c=len(d)-1
    for k in range(0,len(d)):
        if d[k]==d[c]:
            s="True"
        else:
            s = "False"
            break
        c-=1
    print(s)

a = [20,10,0,0,0,10,20,30]
palindrome(a,5,5)
