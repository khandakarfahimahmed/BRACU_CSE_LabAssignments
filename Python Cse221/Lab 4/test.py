from queue import PriorityQueue
import math
j = open("output1.txt","w")
def Dijkstra(adj_list, source):
    pp=[]
    ss=[]
    Q = PriorityQueue()
    visited = [False]*len(adj_list)
    dist = [math.inf]*len(adj_list)
    dist[source] = 0

    Q.put((dist[source], source))
    while not Q.empty():
        u = Q.get()[1]
        if visited[u]:
            continue
        visited[u] = True
        #ss=ss+str(u)+" "
        pp.append(str(u))
        # if len(pp)>3:
        #     pp.remove(2)
        for v in adj_list[u]:
            alt = dist[u] + v[1]
            if alt<dist[v[0]]:
                dist[v[0]] = alt
                Q.put((dist[v[0]],v[0]))
    if len(pp)>3:
        pp.remove("2")
    print(pp)
    return dist[len(adj_list)-1]
f = open("input1.txt",'r')
#j = open("output1.txt","w")
a=[]
b=[]
c=0
s=[]
for i in f:
    c+=1
    if c<5:
        a.append(i)
    else:
        b.append(i)
t = int(a[0])
a=a[1:]
c=[]

for i in range(0,2):
    N, M= a[0].split()
    a=a[1:]
    N = int(N)
    M = int(M)
    adj_list = [[] for x in range(N+1)]

    for j in range(M):
        u, v, w = a[0].split()
        u=int(u)
        v=int(v)
        w=int(w)
        a=a[1:]
        adj_list[u].append((v,w))
    s.append(Dijkstra(adj_list, 1))
for i in range(0,1):
    N, M= b[0].split()
    b=b[1:]
    N = int(N)
    M = int(M)
    adj_list = [[] for x in range(N+1)]

    for j in range(M):
        u, v, w = b[0].split()
        u=int(u)
        v=int(v)
        w=int(w)
        b=b[1:]
        adj_list[u].append((v,w))
    s.append(Dijkstra(adj_list, 1))
