import sys

si = sys.stdin.readline

point = si().rstrip()

x,y = ord(point[0])-ord('a'),int(point[1])-1


def in_range(x,y):
    return x>=0 and x<8 and y>=0 and y<8

# 수평으로 두칸 이동 후 수직으로 한칸 이동
# -> 왼/오 +  상/하 : 4가지
def count(x,y):
    cnt = 0
    
    dxs,dys = [-1,+1,-1,+1],[-2,-2,+2,+2]
    
    for dx,dy in zip(dxs,dys):
        if in_range(x+dx,y+dy):
            cnt+=1
    return cnt + count_2(x,y)

# 수직으로 두칸 이동 후 수평으로 한칸 이동
# -> 상/하 + 왼/오 : 4가지
def count_2(x,y):
    cnt = 0
    
    dxs,dys = [-2,-2,+2,+2],[-1,+1,-1,+1]
    
    for dx,dy in zip(dxs,dys):
        if in_range(x+dx,y+dy):
            cnt+=1
    return cnt

print(count(x,y))