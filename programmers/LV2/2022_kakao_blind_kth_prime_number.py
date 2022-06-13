def get_k_notation(n,k):
    if n<k:
        return str(n)
    return str(get_k_notation(n//k,k)) + str(n%k)

# # 0을 기준으로 나눴기 때문에, 이미 그 숫자를 그대로 바라보면 십진수라고 할 수 있다.
# def get_number(n,k):
#     cnt = len(n)
#     rev = n[::-1]
#     result = 0
    
#     for i in range(cnt):
#         result += int(rev[i])*(k**i)
#     return result

def is_prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
    
def solution(n, k):
    k_not = get_k_notation(n,k)
    candidates = k_not.split('0')
    # numbers = [get_number(i,10) for i in candidates if i!='']
    numbers = [is_prime(int(i)) for i in candidates if i!='']
    answer = sum(numbers)
    return answer
