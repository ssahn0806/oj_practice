from re import L
import sys

si = sys.stdin.readline

# N,M size
N,M = map(int,si().rstrip().split())

# initial point, direction
x,y,cur_dir = map(int,si().rstrip().split())

# current direction
# N(0) : W,S,E,N
# E(1) : N,W,S,E
# S(2) : E,N,W,S
# W(3) : S,E,N,W

# map state

grid = [
    list(map(int,si().rstrip().split()))
    for _ in range(N)
]

# check visit

visited = [
    [0 for _ in range(M)]
    for _ in range(N)
]

visited[x][y] = 1
cnt = 0
dxs,dys = [0,+1,0,-1],[-1,0,+1,0] # N 기준

def in_range(x,y):
    return x>=0 and x<N and y>=0 and y<M
            
while True:
    cnt+=1
    
    # 모든 방향을 확인했음에도 불구하고 이동하지 못한 경우
    if cnt == 5:
        
        # 뒤로 간다의 개념(!!!)
        new_x,new_y = x - dxs[cur_dir], y - dys[cur_dir]
        
        # 현재 방향을 그대로 바라보면서 후진했을 때 갈 수 있는 곳인지 체크
        if not in_range(new_x,new_y) or grid[new_x][new_y]:
            break
        x,y = new_x,new_y
        cnt = 0
        
    cur_dir = (cur_dir+3)%4 # 왼쪽으로 90도 회전
    
    new_x,new_y = x + dxs[cur_dir], y + dys[cur_dir]
    
    # 격자를 벗어나는 경우
    if not in_range(new_x,new_y):
        continue

    # 가지 못하는 공간인 경우
    if grid[new_x][new_y]:
        continue
    
    # 이미 방문한 곳인 경우
    if visited[new_x][new_y]:
        continue
    
    # 갈 수 있는 케이스는 방문체크 해주고 현재 x,y를 갱신
    x,y = new_x,new_y
    visited[x][y] = 1
    cnt = 0     

# 2차원 리스트를 합하는 List comprehension
print(sum([sum(i) for i in visited]))