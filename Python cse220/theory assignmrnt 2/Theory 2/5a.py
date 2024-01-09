def star(a,i=1):
    if i>a:
        return
    else:
        for j in range(1,i+1):
            print(j,end=" ")
        print()
        return star(a,i+1)

star(5)
