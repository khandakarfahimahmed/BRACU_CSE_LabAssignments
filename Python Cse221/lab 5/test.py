f = open("input1.txt",'r')
a=[]
for i in f:
    temp = i.split()
    a.append(temp)
a = a[1:]
for i in range(len(a)):
    a[i][0]= int(a[i][0])
    a[i][1]=int(a[i][1])
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i][1]>a[j][1]:
            temp = a[j]
            a[j]=a[i]
            a[i]=temp
b=[]
b.append(a[0])
c=0
for i in range(0,len(a)):
    if i+1==len(a):
        break
    if b[c][1]<=a[i+1][0]:
        if a[i+1] not in b:
            b.append(a[i+1])
            c+=1

with open('output1.txt', 'w') as j:
    j.write(str(len(b)))
    j.write('\n')
    for line in b:
        j.write(str(line))
        j.write('\n')
