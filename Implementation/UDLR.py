import sys

si = sys.stdin.readline

N = int(si().rstrip())

plans = list(si().rstrip().split())

# NxN 격자 공간을 벗어나는지 판단
def in_range(x,y):
    return x>=1 and x<=N and y>=1 and y<=N

x,y = 1,1

# 이동 계획과 dx,dy 테크닉을 연동하기 위한 딕셔너리
plan_dict = {'U':0,'D':1,'L':2,'R':3}

# U,D,L,R에 따른 x,y 변화량 
dxs,dys = [-1,+1,0,0],[0,0,-1,+1]

# 이동 계획을 하나씩 보면서, 새로운 좌표를 계산하고, 해당 좌표로 이동가능하다면 x,y를 갱신한다.
for plan in plans:
    new_x,new_y = x + dxs[plan_dict[plan]], y + dys[plan_dict[plan]]
    if in_range(new_x,new_y):
        x,y = new_x,new_y
print(x,y)
    
    