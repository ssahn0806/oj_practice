def solution(s):
    s = sorted(s.lstrip('{').rstrip('}').split('},{'),key=len)
    
    n = len(s)
    result = [int(s[0])]
    
    
    for i in range(1,n):
        result.append(set(set(list(map(int,s[i].split(','))))-set(list(map(int,s[i-1].split(','))))).pop())
    return result
    
