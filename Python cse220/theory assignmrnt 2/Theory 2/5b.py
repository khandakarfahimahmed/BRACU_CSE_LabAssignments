def star2(a,i=1):
    if i>a:
        return
    else:
        for k in range(0,a-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(j,end=" ")
        print()
        return star2(a,i+1)

star2(5)
