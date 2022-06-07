import sys

si = sys.stdin.readline

n,m = map(int,si().rstrip().split())

for i in range(m):
    print('*'*n)