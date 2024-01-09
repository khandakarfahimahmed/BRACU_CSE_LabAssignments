class Node:
    def __init__(self,a,b=None,c=None):
        self.element = a
        self.next = b
        self.prev = c

def Rotate(head):
    n = head.next
    c = 0
    temp =0
    while n is not head:
        print(n.element)
        n = n.prev

node5 =Node(1,None)
node4 =Node(2,node5)
node3 =Node(3,node4)
node2 =Node(4,node3)
node1 =Node(5,node2)
head = Node(None,None,None)
head.next = head.prev = head
node5.next = head.next
node1.prev = head
head.next = node1
node1.next.prev = node1
tail = node5
Rotate(head)
