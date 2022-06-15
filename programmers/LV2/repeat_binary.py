def get_binary(n):
    if n<=1:
        return str(n)
    return get_binary(n//2) + str(n%2)
def solution(s):
    answer = [0,0]
    
    while s!='1':
        zero_count = s.count('0')
        answer[0] += 1
        answer[1] += zero_count
        s = get_binary(len(s.replace('0','')))
    return answer