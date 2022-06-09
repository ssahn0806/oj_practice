def solution(arr, divisor):
    answer = []
    
    for e in arr:
        if e%divisor == 0:
            answer.append(e)
    answer.sort()
    
    if not answer:
        return [-1]
    return answer
    