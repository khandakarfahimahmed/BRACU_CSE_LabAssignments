b = int(input("enter M preferred choices: "))
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

a=selection_sort([10, 2, 3, 4 ,1, 100 ,1])
for i in range(0,b):
    print(a[i],end=" ")
