def solution(n):
    result = 0
    for i in range(1,n+1):
        if n % i == 0:
            result += i
            
    # n/2의 수들만 검사하면 성능이 약 2배 향상된다
    
    return result