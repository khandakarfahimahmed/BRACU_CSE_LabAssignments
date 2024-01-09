inp = open('input.txt','r')
num = ['.','1','2','3','4','5','6','7','8','9','0']
f = open('output.txt','w')
g = open('record.txt','w')
elements = 0
odd_parity = 0
even_parity=0
no_parity=0
palindrome=0
non_palindrome=0
d=''
s = ''
s1=''
for line in inp:
    d=line
    elements+=1
    for i in range(0,len(d)):
        if d[i] in num:
            s=s+d[i]

        else:
            s1=s1+d[i]

            print(s1)
    s1 = s1[1:-1]
    temp = 0
    c=0
    for j in range(len(s1)-1,-1,-1):
        if s1=="":
            c+=1
            break
        if s1[j]!=s1[temp]:
            c+=1
            break
        else:
        	pass
        temp+=1

    if c==0:
        palindrome+=1
        try:
            if int(s)%2==0:
                f.write(s+' has even parity and '+s1+" is a palindrome"+'\n')
                even_parity+=1
            else:
                odd_parity+=1
                f.write(s+' has odd parity and '+s1+" is a palindrome"+'\n')
        except:
            no_parity+=1
            f.write(s+' cannot have parity and '+s1+" is a palindrome"+'\n')
    else:
        non_palindrome+=1
        try:
            if int(s)%2==0:
                f.write(s+' has even parity and '+s1+" is not a palindrome"+'\n')
                even_parity+=1
            else:
                odd_parity+=1
                f.write(s+' has odd parity and '+s1+" is not a palindrome"+'\n')
        except:
            no_parity+=1
            f.write(s+' cannot have parity and '+s1+" is not a palindrome"+'\n')

    s=""
    s1=""

g.write("Percentage of odd parity: "+ str(int((100*odd_parity)/elements))+"%"+'\n')
g.write("Percentage of even parity: "+ str(int((100*even_parity)/elements))+"%"+'\n')
g.write("Percentage of no parity: "+ str(int((100*no_parity)/elements))+"%"+'\n')
g.write("Percentage of palindrome: "+ str(int((100*palindrome)/elements))+"%"+'\n')
g.write("Percentage of non-palindrome: "+ str(int((100*non_palindrome)/elements))+"%"+'\n')
