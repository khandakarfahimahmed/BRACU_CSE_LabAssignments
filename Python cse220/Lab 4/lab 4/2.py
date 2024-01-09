class Node:
    def __init__(self,a,b=None,c=None):
        self.elem = a
        self.nxt = b
        self.prev = c
class Stack:
    def __init__(self,r):
        self.r = r
    n=head = None
    def push(self,a):
        if self.head==None:
            self.head =self.n= Node(a,None,None)
        else:
            self.n.nxt = self.n=Node(a,None,self.n)

    def pop(self):
        self.n= self.head
        c = 0
        while True:
            c+=1
            if self.n.nxt==None:
                break
            self.n= self.n.nxt
        self.n= self.head
        i = 0
        while True:
            i+=1
            if c==i:
                self.n.elem= None
                self.n.prev = None
            if self.n.nxt==None:
                break
            self.n= self.n.nxt
    def checkStack(self):
        a = ["[","{","("]
        b = [")","}","]"]
        c = ["()","{}","[]"]
        al=[]
        s1 = []
        s = ""
        count = 0

        for i in range(0,len(self.r)):
            if self.r[i] in a:
                self.push(self.r[i])
            if self.r[i] in b:
                self.q = self.head
                while self.q!=None:
                    count+=1
                    self.q = self.q.nxt
                if count>0:
                    count=0
                    self.n = self.head
                    k= 0
                    while True:
                        k+=1
                        if count==k:
                            s = self.n.elem+self.r
                        if self.n.nxt==None:
                            break
                        self.n= self.n.nxt
                if s in c:
                    self.pop()
                else:
                    self.push(self.r[i])
        self.p = self.head
        while True:
            al.append(self.p.elem)
            if self.p.nxt==None:
                break
            self.p= self.p.nxt
        for i in range(0,len(r)):
            if r[i] in a:
                s1.append(r[i])
            if r[i] in b:
                if len(s1)>0:
                    s = s1[-1]+r[i]
                if s in c:
                    s1 = s1[:-1]
                else:
                    s1.append(r[i])

        if len(s1)>0:
            print("This expression is NOT correct.")
            if s1[0] in b:
                for j in range(0,len(r)):
                    if r[j]==s1[0]:
                        print("Error at character #",str(j+1)+".",s1[0],"- not opened")
                        break
            else:
                a1 = []
                a2 = []
                a3 = []
                for p in s1:
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
                            a1 = a1[:i]+a1[i+1:-1]
                if len(a2)!=0:
                    for i in range(0,len(a2)):
                        if len(a2)==2:
                            s = a2[i]+a2[i+1]
                            if s in c:
                                a2=[]
                        if len(a1)>2:
                            a2 = a2[:i]+a2[i+1:-1]
                if len(a3)!=0:
                    for i in range(0,len(a3)):
                        if len(a3)==2:
                            s = a3[i]+a3[i+1]
                            if s in c:
                                a3=[]
                        if len(a3)>2:
                            a3 = a3[:i]+a3[i+1:-1]
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
r = input()
print(r)
stack1 = Stack(r)
stack1.checkStack()
