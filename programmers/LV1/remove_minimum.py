def solution(arr):
    del arr[arr.index(min(arr))]
    
    if not arr:
        return [-1]
    return arr