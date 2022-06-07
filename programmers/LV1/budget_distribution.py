def solution(d,budget):
    d.sort()
    
    prefix = []
    
    temp = 0
    for req in d:
        temp += req
        if temp> budget:
            break
        prefix.append(temp)
    return len(prefix)