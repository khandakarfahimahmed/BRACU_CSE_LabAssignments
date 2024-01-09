class Node:
    def __init__(self,e,n=None,p=None):
        self.elem = e
        self.nxt = n
        self.prev = p

def insert(head,newElement):
    n = head.nxt
    a = []
    p = None
    temp = None
    if n!=None:
        while True:
            if newElement not in a:
                a.append(newElement)


                break
            else:
                print("the key already exists")
        n = head.nxt
        while True:
            if newElement in a:
                temp = Node(newElement,head,None)
                n.nxt = temp
                break
    else:
        head.nxt = Node(newElement,head,head)


head = Node(None,None,None)

insert(head,2)
