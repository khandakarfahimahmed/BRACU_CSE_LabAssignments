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
def selection_sort(a):
    n= a
    temp = 0
    c = 0
    c1 = []
    val = 0
    while n!=None:
        c+=1
        c1.append(n.data)
        n=n.next
    d = ((c+1)*(c+2))/2
    for i in range(0,int(d)):
        for j in range(i,len(c1)):
            if c1[i]>c1[j]:
                temp = c1[i]
                c1[i] = c1[j]
                c1[j] = temp
    p=a
    k=0
    while p!=None:
        p.data= c1[k]
        k+=1
        p=p.next
    n = a
    while n!=None:
        print(n.data)
        n=n.next
selection_sort(head)
