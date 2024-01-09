class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
node6 = Node(2,None)
node5 = Node(6,node6)
node4 = Node(7,node5)
node3 = Node(8,node4)
node2 = Node(3,node3)
node1 = Node(5,node2)
head = node1
def Bubble_sort(a):
    n= a
    temp = 0
    c = 0
    while n!=None:
        c+=1
        n=n.next
    d = (c*(c-1))/2
    for i in range(0,int(d)):
        n = a
        while True:
            if n.next.data<n.data:
                temp= n.data
                n.data = n.next.data
                n.next.data = temp
            if n.next.next==None:
                break
            n=n.next
    n = a
    while n!=None:
        print(n.data)
        n=n.next
Bubble_sort(head)
