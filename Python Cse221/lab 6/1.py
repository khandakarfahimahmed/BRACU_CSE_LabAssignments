def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dpMatrix = [[0 for k in range(n+1)] for k in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i == 0 or j == 0):
                dpMatrix[i][j] = 0
            elif(X[i-1] == Y[j-1]):
                dpMatrix[i][j] = dpMatrix[i-1][j-1]+1
            else:
                dpMatrix[i][j] = max(dpMatrix[i-1][j], dpMatrix[i][j-1])
    ans = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            ans = X[i-1]+ans
            i -= 1
            j -= 1
        elif dpMatrix[i-1][j] > dpMatrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ans
pubg = {"Y": "Yasnaya","P": "Pochinki","S": "School","R": "Rozhok","F": "Farm","M": "Mylta","H": "Shelter","I": "Prison"}
f = open("input1.txt",'r')
a=[]
for i in f:
    a.append(i)
num = int(a[0])
ans = lcs(a[1], a[2])

c = int((len(ans)/num) * 100)
with open('output1.txt', 'w') as j:
    for i in ans:
        j.write(pubg[i]+" ")
    j.write("\n")
    j.write("Correctness of prediction:" + str(c) + "%")
