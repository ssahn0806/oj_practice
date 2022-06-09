def solution(n):
    dp_table = [-1]*(n+1)
    
    if dp_table[n] != -1:
        return dp_table[n]
    
    dp_table[0] = 0
    dp_table[1] = 1
    
    for i in range(2,n+1):
        dp_table[i] = dp_table[i-2] + dp_table[i-1]
        
    return dp_table[n]%1234567