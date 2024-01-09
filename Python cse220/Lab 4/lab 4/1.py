class Stack:
    def __init__(self):
        self.stack = []
    def push(self,k):
        self.stack.append(k)
        return self.stack
    def pop(self):
        self.stack = self.stack[0:-1]
        return self.stack

stack1 = Stack()
r =  input()
print(r)
a = ["[","{","("]
b = [")","}","]"]
c = ["()","{}","[]"]
s = ""
for i in range(0,len(r)):
    if r[i] in a:
        stack1.push(r[i])
    if r[i] in b:
        if len(stack1.stack)>0:
            s = stack1.stack[-1]+r[i]
        if s in c:
            stack1.pop()
        else:
            stack1.push(r[i])

if len(stack1.stack)>0:
    print("This expression is NOT correct.")
    if stack1.stack[0] in b:
        for j in range(0,len(r)):
            if r[j]==stack1.stack[0]:
                print("Error at character #",str(j+1)+".",stack1.stack[0],"- not opened")
                break
    else:
        a1 = []
        a2 = []
        a3 = []
        for p in stack1.stack:
            if p == "{":
                a2.append(p)
            if p=="}":
                a2.append(p)
            if p == "[":
                a1.append(p)
            if p == "]":
                a1.append(p)
            if p =="(":
                a3.append(p)
            if p == ")":
                a3.append(p)
        if len(a1)!=0:
            for i in range(0,len(a1)):
                if len(a1)==2:
                    s = a1[i]+a1[i+1]
                    if s in c:
                        a1=[]
                if len(a1)>2:
                    a1 = a1[i+1:-1]
        if len(a2)!=0:
            for i in range(0,len(a2)):
                if len(a2)==2:
                    s = a2[i]+a2[i+1]
                    if s in c:
                        a2=[]
                if len(a1)>2:
                    a2 = a2[i+1:-1]
        if len(a3)!=0:
            for i in range(0,len(a3)):
                if len(a3)==2:
                    s = a3[i]+a3[i+1]
                    if s in c:
                        a3=[]
                if len(a3)>2:
                    a3 = a3[i+1:-1]
        if a1==[]:
            pass
        else:
            for i in range(0,len(r)):
                if r[i]==a1[0]:
                    if a1[0] in a:
                        print("Error at character #",str(i+1)+".",a1[0],"- not closed.")
                    else:
                        print("Error at character #",str(i+1)+".",a3[0],"- not opened.")
        if a2==[]:
            pass
        else:
            for i in range(0,len(r)):
                if r[i]==a2[0]:
                    if a2[0] in a:
                        print("Error at character #",str(i+1)+".",a2[0],"- not closed.")
                    else:
                        print("Error at character #",str(i+1)+".",a2[0],"- not opened.")
        if a3==[]:
            pass
        else:
            for i in range(0,len(r)):
                if r[i]==a3[0]:
                    if a3[0] in a:
                        print("Error at character #",str(i+1)+".",a3[0],"- not closed.")
                    else:
                        print("Error at character #",str(i+1)+".",a3[0],"- not opened.")

else:
    print("This expression is correct.")
