arraysize1 = int(input())
arraysize2 = int(input())
a1 = input()
a2 = input()
c=0
for i in a2:
    for j in a1:
        if int(i)>=int(j):
            c+=1
    print(c,end=" ")
    c=0
