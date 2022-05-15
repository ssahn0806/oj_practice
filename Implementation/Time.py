import sys

si = sys.stdin.readline

N = int(si().rstrip())
cnt = 0
for i in range(N+1):
    for j in range(0,60):
        for k in range(0,60):
            hour_str = ('0' + str(i)) if i<10 else str(i)
            min_str = ('0' + str(j)) if j<10 else str(j)
            sec_str = ('0' + str(k)) if k<10 else str(k)
            time_str = hour_str + min_str + sec_str
            if '3' in time_str:
                cnt+=1
print(cnt)