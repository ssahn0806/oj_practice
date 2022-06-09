def is_prime(n):
    for i in range(2,n//2):
        if n%i == 0:
            return False
    return True

# from itertools import combination

# combination(nums,3) : nums에서 3개를 뽑아 조합을 만드는 경우를 iterator로 반환함.
def solution(nums):
    
    cnt = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                prime_candidate = nums[i] + nums[j] + nums[k]
                if is_prime(prime_candidate):
                    cnt+=1
    
    return cnt