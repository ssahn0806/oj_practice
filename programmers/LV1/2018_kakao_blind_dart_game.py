def solution(dartResult):
    # 3번의 기회
    # 각 기회별 0~10점
    # S,D,T 영역이 존재하며, 각 영역은 n제곱(1,2,3)으로 계산
    # 옵션은 있으면 하나, 없을 수도 있음
    # 옵션 * : 해당 점수 및 직전 점수를 각각 2배
        # 첫번째 * : 첫번째 점수만 2배
        # 중첩 * : 중첩 점수는 4배
    # 옵션 # : 해당 점수 마이너스 처리
        # *,# 중첩 시 # 점수 -2배
    
    
    # 점수|보너스|[옵션]

    # 옵션 별 지정 값
    bonus_point = {'S': 1, 'D':2, 'T':3}
    
    # 최종 점수
    result = 0
    
    # 각 기회별 점수
    subresult = [0,0,0]
    
    # 점수,보너스,옵션 분리 객체
    score = [0,0,0]
    bonus = [1,1,1]
    options = ['','','']
    
    temp = ''
    idx = 0
    
    # 문자열을 점수, 보너스 옵션별로 분리
    for i in dartResult:
        if i in bonus_point.keys():
            score[idx] = int(temp)
            temp = ''
            bonus[idx] = bonus_point[i]
            idx+=1
        elif i == '*' or i == '#':
            options[idx-1] = i
        else :
            temp += i
    
    # 각 기회별 점수 계산
    for i in range(3):
        subresult[i] = score[i] ** bonus[i]
        if options[i] == '*':
            if i>0:
                subresult[i-1]*=2
            subresult[i]*=2
        elif options[i] == '#':
            subresult[i]*=-1      

    result = sum(subresult)
        
    return result