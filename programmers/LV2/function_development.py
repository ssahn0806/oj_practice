import math
from collections import deque
def solution(progresses, speeds):
    
    diff = deque([math.ceil((100-i)/j) for i,j in zip(progresses,speeds)])
    result = []
    
    top = diff.popleft()
    cnt = 1
    
    while diff:
        if diff[0]<=top:
            cnt+=1
            diff.popleft()
        else :
            result.append(cnt)
            if not diff:
                break
            cnt = 1
            top = diff.popleft()
    else :
        result.append(cnt)
    return result