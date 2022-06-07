def solution(absolutes,signs):
    result = 0
    
    # 절댓값과 부호를 함께 받아와 부호에 맞는 값을 더함
    for absolute,sign in zip(absolutes,signs):
        result += absolute if sign else -absolute
    
    return result

#   return sum(absolute if sign else -absolute for absolute,sign in zip(absolutes,signs))