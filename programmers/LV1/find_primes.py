def is_prime(n):
    # 2~N-1 , 2~ N//2, 2~ sqrt(N)
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def solution(n):
    cnt = 0
    for i in range(1,n+1):
        if i==1:
            continue
        if is_prime(i):
            cnt+=1
    
    return cnt
    