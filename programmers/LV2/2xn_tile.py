def solution(n):
    dp_table = [0]*(n+1)
    
    if n == 1 or n == 2:
        return n
    
    dp_table[1] = 1
    dp_table[2] = dp_table[1] + 1
    for i in range(3,n+1):
        dp_table[i] = dp_table[i-2]%1000000007 + dp_table[i-1]%1000000007

    return dp_table[n]%1000000007

    
# X = A + B + C

# X % Y = A%Y + B%Y + C%Y 