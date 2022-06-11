def solution(food_times, k):
    # 모든 음식의 개수
    n = len(food_times)
    
    idx = 0
    for i in range(k):
        if sum(food_times) == 0:
            return -1
        while food_times[idx]==0:
            idx = (idx+1)%n 
        
        food_times[idx]-=1
        idx= (idx+1)%n 
        
    if sum(food_times) == 0:
        return -1
    while food_times[idx]==0:
        idx = (idx+1)%n 
    answer = idx+1
    
    return answer