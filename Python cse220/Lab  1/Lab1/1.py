
def shiftLeft(source,k):
    c = 0
    lenght = len(source[k:len(source)])
    for i in range(k,len(source)):
        source[c] = source[i]
        c+=1
    for j in range(lenght,len(source)):
        source[j] = 0
    print(source)
source = [10,20,30,40,50,60]
shiftLeft(source,3)
