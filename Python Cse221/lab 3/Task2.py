f = open("input.txt",'r')
j = open("output2.txt","w")
f = f
a=[]
d = {}
visit=[0]
for i in f:
    a.append(i.split())
n=int(a[0][0])
visit=[0]*n
a= a[1:]
for i in range(0,n):
    d[a[i][0]]= a[i][1:]
def BFS (visited,graph,node,endPoint):
    queue=[]
    visited[int(node)-1]=1
    queue.append(node)
    while (len(queue) != 0):
         m = queue.pop(0)
         j.write(m+' ')
         if endPoint == m:
             break
         for neighbour in graph[m]:
             if visited[int(neighbour)-1]!= 0:
                 pass
             else:
                 visited[int(neighbour)-1] = 1
                 queue.append(neighbour)

BFS(visit,d,"1","12")
