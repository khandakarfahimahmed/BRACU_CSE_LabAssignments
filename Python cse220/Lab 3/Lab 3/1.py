class Node:
    def __init__(self,e,n=None,p=None):
        self.elem = e
        self.nxt = n
        self.prev = p
class Doublylist:
    def __init__(self,head):
        self.head = head


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
node5.nxt = head
l1 = Doublylist(head)
