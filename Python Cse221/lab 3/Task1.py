f = open("input.txt",'r')
j = open("output3.txt","w")
f = f
a=[]
d = {}
for i in f:
    a.append(i.split())
n=int(a[0][0])
a= a[1:]
for i in range(0,n):
    d[a[i][0]]= a[i][1:]
print(d)
