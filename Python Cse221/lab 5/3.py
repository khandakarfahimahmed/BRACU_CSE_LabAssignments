f = open("input3.txt",'r')
jack=[]
jill=[]
main=""
num=[]
string=""
a=[]
jack_worked=0
jill_worked=0
for i in f:
    a.append(i.split())
for i in a[1]:
    num.append(int(i))
for i in a[2]:
    string=string+i
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            temp = num[j]
            num[j]=num[i]
            num[i]=temp
for i in string:
    if i=="J":
        jack.append(num[0])
        jack_worked=jack_worked+num[0]
        num=num[1:]
        if len(jack)>0:
            main=main+str(jack[len(jack)-1])
    if i=="j":
        if len(jack)>0:
            jill.append(jack[len(jack)-1])
            jill_worked=jill_worked+jack[len(jack)-1]
            main=main+str(jack[len(jack)-1])
            jack.pop(len(jack)-1)
with open('output3.txt', 'w') as j:
    j.write(main+'\n')
    j.write("Jack will work for "+str(jack_worked)+" hours"+'\n')
    j.write("Jill will work for "+str(jill_worked)+" hours")
