def powerN(a,b,i=1,temp=0):
    if i==1:
        temp=a
    if i==b:
        return a
    else:
        return powerN(a*temp,b,i+1,temp)
print(powerN(5,2))
print(powerN(5,3))
print(powerN(5,4))
