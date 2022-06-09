from collections import deque

def solution(priorities, location):
    n = len(priorities)
    # 원본 값과 인덱스를 기억
    q = deque([(priorities[i],i) for i in range(n)])
    result = 1
    while True:
        top_print = q.popleft()
        
        if not q:
            return result
        remain_max = max(q)[0]
        
        if top_print[0] >= remain_max:
            if top_print[1] == location:
                return result
            result+=1
            
        else :
            q.append(top_print)
            
