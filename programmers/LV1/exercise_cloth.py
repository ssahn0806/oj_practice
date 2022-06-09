def solution(n, lost, reserve):
    real_reserve = list(set(reserve) - set(lost))
    real_lost = list(set(lost) - set(reserve))
    
    can_particiate = [1]*(n+1)
    
    for lost_num in real_lost:
        can_particiate[lost_num]-=1
    
    for reserve_num in real_reserve:
        if reserve_num > 1 and reserve_num < n:  
            if can_particiate[reserve_num-1] == 0:
                can_particiate[reserve_num-1]+=1
            else:
                if can_particiate[reserve_num+1] == 0:
                    can_particiate[reserve_num+1]+=1
        elif reserve_num == 1:  
            if can_particiate[reserve_num+1] == 0:
                can_particiate[reserve_num+1]+=1
        else :
            if can_particiate[reserve_num-1] == 0:
                can_particiate[reserve_num-1] +=1
    
    return sum(can_particiate[1:])