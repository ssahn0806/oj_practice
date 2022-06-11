from collections import deque

class Graph():
    def __init__(self,N):
        self.N = N
    
    def add_edge(self,x,y):
        pass
    
    def is_x_y_con(self,x,y):
        pass
    
    def get_con_by_x(self,x):
        pass
    
class List(Graph):
    def __init__(self,N):
        super().__init__(N)
        self.con = [
            []
            for _ in range(N+1)
        ]
    
    def add_edge(self,x,y):
        self.con[x].append(y)
        self.con[y].append(x)
    
    def is_x_y_con(self,x,y):
        return y in self.con[x]
    
    def get_con_by_x(self,x):
        return self.con[x]

def solution(n, edge):
    G = List(n)
    
    for v1,v2 in edge:
        G.add_edge(v1,v2)
    
    visited = [0]*(n+1)
    
    q = deque()
    
    q.append(1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for v in G.get_con_by_x(x):
            if not visited[v]:
                visited[v] = visited[x]+1
                q.append(v)
    
    return visited.count(max(visited))