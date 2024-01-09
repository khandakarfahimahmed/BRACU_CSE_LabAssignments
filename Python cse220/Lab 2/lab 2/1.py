class Node:
    def __init__(self,a,b):
        self.element = a
        self.next = b
class Mylist:
    def __init__(self,head):
        self.head = head

node2 =Node(20,None)
node1 =Node(10,node2)
head = node1
