def insertion_sort(a,i=0,c=0,b=[]):
    if len(a) == c:
        return b
    else:
        b.append(a[i])
        if len(b)>1:
            for j in range(len(b)-1,0,-1):
                if b[j] < b[j-1] :
                    temp = b[j]
                    b[j]=b[j-1]
                    b[j-1]=temp
            return insertion_sort(a,i+1,c+1,b)
        else:
            return insertion_sort(a,i+1,c+1,b)
print(insertion_sort([5,3,8,6,7,2]))
