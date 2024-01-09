def fridayFun(inp,dice,arr=[],c=0,d=0,k=0):
    if d==0:
        d=1
        for i in range(1,inp+1):
            arr.append(i)
    z = 0
    for i in range(0,len(arr)):
        if arr[i]!=0:
            z+=1
    if z==1:
        for i in range(0,len(arr)):
            if arr[i]!=0:
                return arr[i]
    else:
        if k==len(dice):
            k=0
        b= int(dice[k])

        if b==2 or b==4:
            if c==len(arr):
                c=0
            for j in range(c,len(arr)):
                if arr[j]!=0:
                    arr[j] = 0
                    break
                elif j+1==len(arr):
                        j=-1
            if c==len(arr):
                return fridayFun(inp,dice,arr,0,1,k+1)
            else:
                return fridayFun(inp,dice,arr,c,1,k+1)
        else:
            if c==len(arr):
                return fridayFun(inp,dice,arr,0,1,k+1)
            else:
                return fridayFun(inp,dice,arr,c+1,1,k+1)
print(fridayFun(3,"152"))
