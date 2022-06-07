def solution(n):
    result = sorted(list(map(int,str(n))),reverse=True)
    
    return int(''.join(map(str,result)))