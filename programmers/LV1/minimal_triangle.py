# 1개 이상 10000개 이하의 명함 
# 각 원소는 [w,h] 가로,세로에 해당 1~1000


# 모든 명함을 수납할 수 있는 방법 - 가장 긴 가로, 가장 긴 세로를 택함

# 추가 조건 : 크기를 최소화 - 

def solution(sizes):
    n = len(sizes)
    
    width = [max(i,j) for i,j in sizes]
    height = [min(i,j) for i,j in sizes]
    
    # origin_max = max(width)*max(height)
    
    # for i in range(n):
    #     width[i],height[i] = height[i],width[i]
        
    #     if max(width)*max(height) >= origin_max:
    #         width[i],height[i] = height[i],width[i]
    #     else :
    #         origin_max = max(width)*max(height)
    
    # return origin_max
    
    return max(width)*max(height)