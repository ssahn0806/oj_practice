from collections import deque

def in_range(x,y,n,m):
    return x>=0 and x<n and y>=0 and y<m
            
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

    q = deque()
    
    visited[0][0] = 1
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        
        dxs,dys = [0,0,+1,-1],[+1,-1,0,0]
        
        for dx,dy in zip(dxs,dys):
            new_x,new_y = x + dx, y + dy
            if in_range(new_x,new_y,n,m) and visited[new_x][new_y] == 0 and maps[x][y]==1:
                visited[new_x][new_y] = visited[x][y] + 1
                q.append((new_x,new_y))
    return -1 if not visited[n-1][m-1] else visited[n-1][m-1]
    