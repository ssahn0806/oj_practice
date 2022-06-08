def solution(N, stages):
    
    # 전체 사용자 수
    total = len(stages)
    
    
    # 임시 리스트
    temp = []
    
    # 각 스테이지 별로 확인
    for i in range(1,N+1):
        # 현재 스테이지에 머물러있는 사람(클리어하지 못함)
        not_clear = stages.count(i)
        
        # 현재 스테이지이상에 도달한 사람 (마지막 값 고려 1미만시 1로 부여)
        clear = total if total>0 else 1
        
        # 전체 사용자수를 감소시킴(현재 스테이지 클리어 못한 사람 제외)
        total -= not_clear
        
        # 현재 스테이지 번호와, 실패율을 임시 리스트에 넣음
        temp.append((i,not_clear/clear))
    
    # 실패율이 높은 순, 번호가 낮은 순으로 정렬
    temp.sort(key = lambda x : (-x[1],x[0]))
    
    # 번호만 추출
    answer = [i for i,j in temp]
    return answer