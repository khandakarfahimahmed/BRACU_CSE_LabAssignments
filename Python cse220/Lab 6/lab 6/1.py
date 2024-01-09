def selection_sort(a,i=0,c=0):
    if ((len(a)+1)*(len(a)+2))/2 == c:
        return a
    else:
        for j in range(i,len(a)):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        return selection_sort(a,i+1,c+1)

print(selection_sort([5,3,8,6,7,2]))
