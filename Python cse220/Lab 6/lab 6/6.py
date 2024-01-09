def binary_search(a,elem,c=0,s=0,l=0,u=0):
    m=0
    if c==0:
        d = ((len(a)+1)*(len(a)+2))/2
        for i in range(0,int(d)):
            for j in range(i,len(a)):
                if a[i]>a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
        l=0
        u = len(a)-1
        c=5

    m = (u+l)//2
    if a[m]==elem:
        return m
    else:
        if elem<a[m]:
            u = m-1
        else:
            l= m+1
        return binary_search(a,elem,c,s,l,u)

print(binary_search([1,2,3,4,5,6],3))
