def solution(price,money,count):
    
    # 횟수에 따른 금액 차감
    for i in range(1,count+1):
        money -= price*i
    
    # 남은 돈이 음수이면 해당 금액만큼 부족한 것
    result = -money if money < 0 else 0
    
    return result    