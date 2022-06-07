def solution(array, commands):
    
    # 정답
    answer = []
    
    
    # 각 명령어 집합에 대하여
    for i in range(len(commands)):
        
        # 시작 위치
        start = commands[i][0]
        
        # 끝 위치
        end = commands[i][1]
        
        # K
        k = commands[i][2]
        
        
        # 시작위치와 끝위치가 같으면 원소 하나
        if start == end:
            temp = array[start-1]
            answer.append(temp)
            
        # 다르면 슬라이싱 후 정렬 및 K번째 원소 찾기
        else :
            temp = array[start-1:end]
            temp.sort()
            answer.append(temp[k-1])
            
    return answer