def remove(source,size,idx):

    for j in range(idx,len(source)-1):
        source[j]=source[j+1]
    print(source)

source = [10,20,30,40,50,0,0]
remove(source,5,2)
