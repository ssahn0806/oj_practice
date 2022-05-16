import sys
from collections import deque

si = sys.stdin.readline

N,M = map(int,si().rstrip().split())

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
    
    if grid[x][y] == '0' or visited[x][y]!=0:
        return False

    return True

# 가중치가 동일한 그래프에서 최단 경로는 BFS를 이용하면 된다.
def bfs():
    while q:
        x,y = q.popleft()
        
        dxs,dys = [-1,+1,0,0],[0,0,-1,+1]
        
        for dx,dy in zip(dxs,dys):
            new_x,new_y = x + dx, y + dy
            if can_go(new_x,new_y):
                # 새롭게 방문할 수 있는 곳은 현재 칸까지 오는데 든 비용에 1을 추가해서 기록한다.
                visited[new_x][new_y] = visited[x][y] + 1
                q.append((new_x,new_y))
                

# 시작 지점과 도착지점도 카운팅 횟수에 포함되므로 1로 시작
visited[0][0] = 1
q.append((0,0))
bfs()
print(visited[N-1][M-1])