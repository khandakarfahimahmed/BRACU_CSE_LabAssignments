a = [1,1,1,2,1]
sum1 = 0
sum2 = 0
s = "false"
for i in range(0,len(a)):
    for j in range(0,i+1):
        sum1 = sum1 + a[j]
    for k in range((i+1),len(a)):
        sum2 = sum2 + a[k]

    if sum1==sum2:
        s= "true"
        break
    sum1=0
    sum2 = 0

print(s)
