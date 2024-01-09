f = open("input.txt",'r')
j = open("output3.txt","w")
f = f
a=[]
d = {}
visit=[0]
for i in f:
    a.append(i.split())
n=int(a[0][0])
visited=[0]*n
printed=[]
a= a[1:]
for i in range(0,n):
    d[a[i][0]]= a[i][1:]
def DFS_VISIT(graph,node):
    visited[int(node)-1]=1
    printed.append(node)
    for n in graph[node]:
        if node not in visited:
            DFS_VISIT(graph,n)
def DFS(graph,endPoint):
    for n in graph:
        if n not in visited:
            DFS_VISIT(graph,n)
    for i in printed:
        j.write(str(i)+" ")
        if i==endPoint:
            break
DFS(d,"12")
