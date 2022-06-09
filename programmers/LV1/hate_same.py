# Stack
def solution(arr):
    result = [arr[0]]
    
    n = len(arr)
    
    for i in range(1,n):
        if result[-1] == arr[i]:
            continue
        result.append(arr[i])
    return result