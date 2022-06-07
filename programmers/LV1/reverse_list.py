def solution(n):
    answer = [int(i) for i in str(n)[::-1]]
    
    # list(map(int,reversed(str(n))))
    return answer