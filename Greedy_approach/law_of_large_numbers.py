import sys
 
si = sys.stdin.readline
 
N,M,K = map(int,si().rstrip().split())
 
numbers = list(map(int,si().rstrip().split()))
 
# 가장 큰 값을 더하는 것이 최선이므로 내림차순으로 정렬
numbers.sort(reverse=True)
 
max_v = 0
cnt = 0

# 총 더하는 시행의 횟수가 M번이 되기 전까지 반복
while cnt<M:
    # 가장 큰값과 그 다음으로 큰 값이 같다면, K번의 횟수 제한에 영향을 받지 않는다.
    if numbers[0] == numbers[1]:
        max_v = numbers[0]*M
        break
    else :
    # 한 인덱스의 값은 최대 K번 연속해서 더할 수 있으므로, 그 주기마다 두번째로 큰수를 한번 더해준다.
        if cnt>0 and cnt%K == 0:
            max_v += numbers[1]
        else :
            max_v += numbers[0]
    cnt+=1

print(max_v)
