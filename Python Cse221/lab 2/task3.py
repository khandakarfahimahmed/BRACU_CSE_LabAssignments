d = [1,2,3,4,5,6]
d2 = [50,60,80,20,10,30]
def insertion_sort(a,i=0,c=0,b=[]):
    if len(a) == c:
        return b
    else:
        b.append(a[i])
        if len(b)>1:
            for j in range(len(b)-1,0,-1):
                if b[j] > b[j-1] :
                    temp = b[j]
                    b[j]=b[j-1]
                    b[j-1]=temp
            return insertion_sort(a,i+1,c+1,b)
        else:
            return insertion_sort(a,i+1,c+1,b)
a=insertion_sort(d2)
c=[]
for i in range(0,len(d2)):
    for j in range(0,len(a)):
        if a[i]==d2[j]:
            if len(c)==len(d):
                break
            c.append(d[j])

print(c)
