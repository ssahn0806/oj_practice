import sys

si = sys.stdin.readline

N,M = map(int,si().rstrip().split())

x,y,d = map(int,si().rstrip().split())

grid = [
    list(map(int,si().rstrip().split()))
    for _ in range(N)
]

def in_range(x,y):
    return x>=0 and x<N and y>=0 and y<M

visited = [
    [0 for _ in range(M)]
    for _ in range(N)
]
    
visited[x][y] = 1

# 방향의 우선순위 : 현재 보고있는 방향의 반시계 90도 부터 확인

# 북 (0) : 서,남,동,북
# 동 (1) : 북,서,남,동
# 남 (2) : 동,북,서,남
# 서 (3) : 남,동,북,서

dxs,dys = [0,+1,0,-1],[-1,0,+1,0]

start_idx = (4-d)%4 

can_travel = True

# while can_travel:
#     new_x,new_y = x + dxs[start_idx],y + dys[start_idx]
    
#     if not in_range(new_x,new_y):
#         start_idx = (start_idx+1)%4
#         continue
    
#     if not visited[new_x][new_y]:
#         d = 
        
