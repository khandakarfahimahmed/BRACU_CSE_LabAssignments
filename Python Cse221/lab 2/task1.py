a = [10,20,5,15,25,30]
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)

c=0
for i in range(0,len(a)-1):
    if a[i]<a[i+1]:      #the fist condition of this loop is for best case scenario and it's time complexity is θ(n)
        pass             #if user enters a sorted list then because of it's condition it will run for θ(n) times ans it is the best case scenario
    else:                # But if user enters a unsorted list then the code's complexity will become θ(n^2), which is the worst case scenario
        c=1
        bubbleSort(a)
if c==0:
    print(a)
