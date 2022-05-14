import sys

si = sys.stdin.readline

N,M = map(int,si().rstrip().split())

grid = [
    list(map(int,si().rstrip().split()))
    for _ in range(N)
]

# 각 행을 순회하면서 최솟값을 기록한다.
col_max = []
for i in range(N):
    col_max.append(min(grid[i]))

# 기록되어 있는 최솟값 중에서 최댓값을 선택한다.
print(max(col_max))
