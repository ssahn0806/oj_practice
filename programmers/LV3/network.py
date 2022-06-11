from collections import deque

def bfs(q,G,V):
    while q:
        x = q.popleft()
        for v,e in enumerate(G[x]):
            if e == 1 and V[v] == 0:
                V[v] = 1
                q.append((v))
        
def solution(n, computers):
    
    for i in range(n):
        for j in range(n):
            computers[i][j] = (0 if i==j else computers[i][j])
            
    q = deque()
    visited = [0]*(n+1)
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            q.append((i))
            visited[i] = 1
            bfs(q,computers,visited)
            cnt+=1
        
        
    return cnt