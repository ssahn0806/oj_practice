def solution(msg):
    # 영어 대문자만 처리한다고 가정.
    
    # 길이가 1인 모든 단어를 퐇마하도록 사전을 초기화 한다.
    my_dict = {chr(ord('A')+i): i+1 for i in range(26)}
    
    
    
    
        
    answer = []
    n = len(msg)
    start_idx = 0
    
    
    def find_maximum_str(start_idx):
        # start_idx부터 하나씩 길이를 늘려가며, 사전에 존재하는 최대 길이의 문자열을 반환한다.
        # 삭제해야할 마지막 위치도 함께 반환한다.
        for i in range(n-start_idx):
            # start_idx + 0 
            # start_idx + n - start_idx - 1 = n-1 
            if msg[start_idx:start_idx+i+1] not in my_dict:
                return msg[start_idx:start_idx+i],start_idx+i
            
        # 모두 통과했다면, 전체 문자열이 그 자체가 된다.
        return msg[start_idx:],n
    
    while True:    
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열(w)을 찾는다.  
        w,next_idx = find_maximum_str(start_idx)
        # w에 해당하는 사전의 색인 번호를 출력하고, 
        answer.append(my_dict[w])
        
        # 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.  
        # 단계 2로 돌아간다.
        if next_idx < n:
            my_dict[msg[start_idx:next_idx+1]] = len(my_dict)+1
            # 입력에서 w를 제거한다.
            start_idx = next_idx
            
        else :
            break
       
    return answer
    

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))