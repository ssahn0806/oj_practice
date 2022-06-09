import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    answer = 0
    while True:
        
        if len(scoville)==1 and scoville[0]<K:
            return -1
        
        if scoville[0]>=K:
            return answer
        f1 = heapq.heappop(scoville)
        f2 = heapq.heappop(scoville)

        mixed_f = f1 + f2*2
        heapq.heappush(scoville,mixed_f)    
        answer+=1
    return answer