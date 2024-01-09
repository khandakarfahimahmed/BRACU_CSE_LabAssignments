class Node:
    def __init__(self,e,n=None,p=None):
        self.elem = e
        self.next = n
        self.prev = p

def insert(head,newElement,index):
    n = head.next
    s = ""
    c = 0
    p = None
    temp =None
    while True:
        c+=1
        if n.next==head:
            break
        n = n.next
    n=head.next

    if index<=c:
        while True:
            if n.elem==newElement:
                s = "The key already exists"
                print(s)
                break
            if n.next==head:
                break
            n = n.next
    n = head.next
    if index<=c:
        c=1
        if s!= "The key already exists":
            p = head.next
            while True:
                c+=1
                if c==index:
                    temp = p.next
                    p.next = Node(newElement,temp,p)
                if p.next==head:
                    break
                p = p.next
    while True:
        print(n.elem)
        if n.next==head:
            break
        n = n.next
    n=head.next

node5 =Node(5,None,None)
node4 =Node(4,node5,None)
node3 =Node(3,node4,None)
node2 =Node(2,node3,None)
node1 =Node(1,node2,None)
head = Node(None,node1,node5)
node1.prev = head
node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4
node5.next = head
insert(head,0,4)
