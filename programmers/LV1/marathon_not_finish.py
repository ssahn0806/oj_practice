def solution(participant, completion):
    
    result = []
    
    participants = {}
    
    # 마라톤 참가자의 수를 딕셔너리로 저장
    for person in participant:
        if person in participants.keys():
            participants[person]+=1
        else :
            participants[person]=1
    
    # 완주자의 수만큼 차감
    for person in completion:
        participants[person]-=1
    
    # 완주자인 경우 카운팅이 0이므로 존재하는 경우 낙오자
    result = [name for name,val in participants.items() if val]
    
    return result[0]