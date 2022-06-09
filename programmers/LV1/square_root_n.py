def solution(n):
    root_n = n**0.5
    
    # 제곱근 수라면 1로 나눈 나머지가 0이다 : 소숫점이 존재하지 않는다
    
    # float.is_integer()
    
    if root_n == int(root_n):
        return (root_n+1)**2
    else :
        return -1