import sys

si = sys.stdin.readline

N = int(si().rstrip()) # 500 이하

numbers = [int(si().rstrip()) for _ in range(N)]

numbers.sort(reverse=True)

print(' '.join(map(str,numbers)))