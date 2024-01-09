def LCS(a,b,c):
    m = len(a)
    n = len(b)
    o = len(c)

    dp = [ [ [0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            for k in range(1,o+1):
                dp[i][j][k] = max([dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1]]);

                if a[i-1]==b[j-1] and b[j-1]==c[k-1]:
                    dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-1][k-1]+1)

    return dp[m][n][o]

f = open("input2.txt",'r')
a=[]
for i in f:
    a.append(i)
p=LCS(a[0], a[1], a[2])
j = open("output2.txt","w")
j.write(str(p))
