def solution(nums):
    n = len(nums)//2
    num_set = set(nums)
    m = len(num_set)
    
    return n if m>n else m