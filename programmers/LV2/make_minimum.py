# 두 배열을 하나는 오름차순, 하나는 내림차순으로 정렬한 뒤 순서대로 곱해야 최솟값을 보장할 수 있다.

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    result = 0
    n = len(A)
    for i in range(n):
        result += A[i]*B[i]
        
    return result