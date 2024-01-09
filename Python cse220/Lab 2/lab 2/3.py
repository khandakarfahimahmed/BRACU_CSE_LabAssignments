#task_03
class Node:
    def __init__(self,a,b=None):
        self.element = a
        self.next = b

def EvenNumber(startingNode):
    n = startingNode
    c=0
    temp = None
    newNode= None
    while n!=None:
        if temp!=None:
            if n.element%2==0:
                newNode.next = Node(n.element,None)
                c+=1
        else:
            if n.element%2==0:
                temp = Node(n.element,None)
                newNode = temp
                c+=1
        n=n.next
    if c>0:
        while newNode is not None:
            print(newNode.element)
            newNode = newNode.next
#==========

def listOrNot(startingNode,checkingValue):
    n = startingNode
    c=0
    while n is not None:
        if n.element==checkingValue:
            c+=1
        n=n.next
    if c>0:
        print("True")
    else:
        print("False")
#===========
def reverse(head):
    n = head
    prev = None
    while n is not None:
        nxt = n.next
        n.next = prev
        prev = n
        n = nxt
    head1 = prev
    while head1 is not None:
        print(head1.element)
        head1 = head1.next
#=========
def sort(head):
    n = head
    a=[]
    while n is not None:
        a.append(n.element)
        n = n.next
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    n= head
    i=0
    while n is not None:
        n.element = a[i]
        print(a[i])
        n = n.next
        i+=1

    n = head
    while n is not None:
        print(n.element)
        n = n.next
#=======
def sumlist(head):
    n = head
    sum=0
    while n is not None:
        sum=sum+n.element
        n = n.next
    print(sum)


node5 =Node(8,None)
node4 =Node(3,node5)
node3 =Node(5,node4)
node2 =Node(2,node3)
node1 =Node(1,node2)
head = node1
n = head

EvenNumber(head)
listOrNot(head,7)
sort(head)
sumlist(head)
reverse(head)
