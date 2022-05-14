import sys

si = sys.stdin.readline

N,K = map(int,si().rstrip().split())

cnt = 0

while N!=1:
    # N이 K로 나누어 떨어진다면 1을 빼는 것에 비해 N을 줄이는 영향이 크다.
    if N%K==0:
        N//=K
    # 그렇지 않다면 1을 빼는 선택밖에 할 수 없다.
    else :
        N-=1
    cnt+=1
print(cnt)