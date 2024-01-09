class Node:
    def __init__(self,e,n=None,p=None):
        self.elem = e
        self.nxt = n
        self.prev = p
def showList(head):
    n = head.nxt
    if head.nxt==None:
        print("Empty list")
        return
    while True:
        print(n.elem)
        if n.nxt==head:
            break
        n = n.nxt

head = Node(None,None,None)
showList(head)
