class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev=prev
node6 = Node(2,None)
node5 = Node(6,node6)
node4 = Node(7,node5)
node3 = Node(8,node4)
node2 = Node(3,node3)
node1 = Node(5,node2)
node1.prev = node6
node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5

head = node1
def insertion_sort(a):
    n= a
    temp = 0
    c = 0
    c1=[]
    b=[]
    while n!=None:
        c+=1
        c1.append(n.data)
        n=n.next
    for i in range(0,c):
        b.append(c1[i])
        if len(b)>1:
            for j in range(len(b)-1,0,-1):
                if b[j] < b[j-1] :
                    temp = b[j]
                    b[j]=b[j-1]
                    b[j-1]=temp
    p=a
    k=0
    while p!=None:
        p.data= b[k]
        k+=1
        p=p.next

    n = a
    while n!=None:
        print(n.data)
        n=n.next
insertion_sort(head)
