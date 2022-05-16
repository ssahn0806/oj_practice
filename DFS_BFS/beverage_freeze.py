import sys
from collections import deque


si = sys.stdin.readline

N,M = map(int,si().rstrip().split())


# 2차원 격자가 공백없이 주어지는 경우의 문제는 각 칸을 문자열로 생각한다.
grid = [
    list(si().rstrip())
    for _ in range(N)
]

visited = [
    [0 for _ in range(M)]
    for _ in range(N)
]

q = deque()
def in_range(x,y):
    return x>=0 and x<N and y>=0 and y<M

def can_go(x,y):
    
    if not in_range(x,y):
        return False
    
    # 2차원 격자가 공백없이 주어지는 경우의 문제는 각 칸을 문자열로 생각한다.
    if grid[x][y] == '1' or visited[x][y]!=0:
        return False
    
    return True

def bfs(value):
    while q:
        x,y = q.popleft()
        dxs,dys = [-1,+1,0,0],[0,0,-1,+1]
        
        for dx,dy in zip(dxs,dys):
            new_x,new_y = x + dx, y + dy
            if can_go(new_x,new_y):
                    visited[new_x][new_y] = value
                    q.append((new_x,new_y))
    
cnt = 1                
for i in range(N):
    for j in range(M):
        # 완전탐색처럼 전체 격자를 순회하면서, 얼릴 수 있는 곳이면서 아직 방문하지 않은 곳인 경우에만 bfs 수행 후 갯수 증가
        if grid[i][j] == '0' and not visited[i][j]:
            visited[i][j] = 1
            q.append((i,j))
            bfs(cnt)
            cnt+=1

print(cnt-1)
