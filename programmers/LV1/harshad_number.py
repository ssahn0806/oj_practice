def solution(x):
    digit_sum = sum(int(i) for i in str(x))
    
    return x%digit_sum == 0