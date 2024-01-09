class Node:
    def __init__(self,e,n=None,p=None):
        self.elem = e
        self.nxt = n
        self.prev = p

class MyList:
    def __init__(self,a):
        self.head = a
    def __intit__(self,a):
        n = self.head
        self.a = a
        c = 0
        temp = None
        n1 = Node(a[0],None,n)
        n.nxt = n1
        for i in range(1,len(a)):
            n1.nxt = n1 = Node(a[i],None,n1)
            c+=1
            if c==len(a)-1:
                n1.nxt = n
                n.prev = n1
        p = n.nxt
        temp = n
        while True:
            print(p.elem)
            if p.nxt ==temp:
                break
            p = p.nxt

head = Node(None,None,None)
a = [1,2,3,4,5]
l1 = MyList(head)
l1.__intit__(a)
