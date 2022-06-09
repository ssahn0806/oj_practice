def solution(n):
    dp_table = [-1]*(n+1)
    
    if n<3:
        return n
    
    dp_table[1] = 1
    dp_table[2] = 1 + 1

    # dp_table[3] = dp_table[1] + dp_table[2]
    for i in range(3,n+1):
        dp_table[i] = dp_table[i-2] + dp_table[i-1]
    
    return dp_table[n]%1234567