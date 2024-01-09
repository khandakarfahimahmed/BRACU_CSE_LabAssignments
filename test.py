n = int(input("Enter a number :"))
i = 1
while i<=(2*n)-1:
	j =1
	while (i<=n and j<=(i-1)+n) or (i>n and j<=3*n-i-1):
		if (i< n and j<=n-i) or (i>n and j<=i-n):
			print(" ",end="")
		elif (i<n and j>=n-i+2 and j<=(i-2)+n) or (i>n and j>=i-n+2 and j<=3*n-i-2):
			print(" ",end="")
		else:
			print("*",end="")


		j+=1
	print("")
	i+=1