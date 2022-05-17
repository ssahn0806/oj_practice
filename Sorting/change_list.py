import sys

si = sys.stdin.readline

N,K = map(int,si().rstrip().split()) # 100000

lst_A = list(map(int,si().rstrip().split()))
lst_B = list(map(int,si().rstrip().split()))

lst_A.sort()
lst_B.sort(reverse=True)

cnt = 0
for i in range(N):
    if cnt == K:
        break
    if lst_A[i] < lst_B[i]:
        lst_A[i],lst_B[i] = lst_B[i],lst_A[i]
        cnt+=1

print(sum(lst_A))