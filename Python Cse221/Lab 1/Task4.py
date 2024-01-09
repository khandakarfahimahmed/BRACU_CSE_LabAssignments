c= [[0,0,0],
    [0,0,0],
    [0,0,0]]
f = open("input.txt",'r')
a=0
d=0
b=0
dig = [0,1,2,3,4,5,6,7,8,9]

for i in f:
	if a==0:
		n= int(i)
		A=[[]]*n
		B=[[]]*n
	else:
		if a<n+1:
			temp=[]
			for k in i:
				if k!=" " and k!="\n":
					temp.append(int(k))
			A[b]=temp
			b+=1
		if a>n and a<n**2:
			temp = []
			for k in i:
				if k!=" " and k!="\n":
					temp.append(int(k))
			B[d]=temp
			d+=1
	a+=1
n+=1
for i in range(0,n-1):
	for j in range(0,n-1):
		for k in range(0,n-1):
			c[i][j] = c[i][j]+ A[i][k]*B[k][j]
j = open("output4.txt","w")
s=""
for p in c:
	for i in p:
		s=s+str(i)+" "
	j.write(s+'\n')
	s=""
