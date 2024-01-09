def merge(l,r):
    a=[]
    b=0
    c=0
    while b<len(l) and c<len(r):
        if l[b]<=r[c]:
            a.append(l[b])
            b+=1
        else:
            a.append(r[c])
            c+=1
    a+=l[b:]
    a+=r[c:]
    return a
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid= int(len(arr)/2)
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])
    return merge(l,r)
a = [10,20,3,40,5,6]
print(merge_sort(a))
