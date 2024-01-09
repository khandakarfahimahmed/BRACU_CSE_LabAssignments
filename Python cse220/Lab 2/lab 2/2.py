class Mylist:
    def __init__(self,a,b):
        self.data = a
        self.next = b

class Mylist:
    def __init__(self,head):
        self.a = [1,2,3,4,5]
        n = head
        i=0
        while n is not None:
            n.data = a[i]
            n = n.next
            i+=1

class Mylist:
    def __init__(self,head):
        n = head
        newnode = Node()
        while n is not None:
            newnode=n.data
            newnode.next = n.next
            n = n.next
#2=========
def showList(self,head):
    c=0
    n = head
    while n is not None:
        print(n.data)
        n = n.next
        c+=1
    if c!>0:
        print("Empty list")

#3=======
def isEmpty(self,head):
    c=0
    n = head
    while n is not None:

        n = n.next
        c+=1
    if c!>0:
        print("False")
    else:
        print("True")
#4=====
def clear(self,head):
    n = head
    while n is not None:
        n.data = None
        n = n.next
#5====
def insert(self,newElement,3):
    self.newElement = newElement
    self.index = 3
    n = head
    c=0
    while n is not None:
        c+=1
        n = n.next
    if c==self.index or c>sel.index or c<self.index-1:
        print("key already axist and dont insert the key")
    else:
        n = head
        i=0
        while i!=self.index+1:
            if i==3:
                n.next = Node(sel.newElement,None)
                break
            n=n.next
#6======
def insert(self,newElement,index=4):
    self.newElement = newElement
    self.index = index
    n = head
    c=0
    while n is not None:
        c+=1
        n = n.next
    if c==self.index or c>sel.index or c<self.index-1:
        print("key already axist and dont insert the key")
    else:
        n = head
        i=0
        while i!=self.index+1:
            if i==self.index:
                n.next = Node(sel.newElement,None)
                break
            n=n.next
            i+=1
#7====
def remove(self,deletekey=4):
    self.deletekey = deletekey
    n = head
    c = 0
    while n is not None:
        c+=1
        n=n.next
    if c==sel.deletekey:
        n= head
        c=0
        while n is not None:
            if c+1==self.deletekey:
                break
            n=n.next
            c+=1
    else:
        n= head
        c=0
        prev=None
        while n is not None:
            if c<self.deletekey:
                prev = n
                print(prev.data)
            if c>self.deletekey:
                prev.next = n
                print(prev.data)
            n=n.next
            c+=1
