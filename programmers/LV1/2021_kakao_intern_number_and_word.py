def solution(s):
    # 숫자와 단어로 이루어진 문자열 s가 주어짐
    
    n = len(s)
    
    # 숫자와 문자 대응 관계 
    num_dict = {'zero':'0','one':'1','two':'2',
                'three':'3','four':'4','five':'5',
                'six':'6','seven':'7','eight':'8',
               'nine':'9'}
    
    # 정답
    answer = ''
    
    # 임시 저장 객체
    temp = ''
    
    # O(N)
    for i in range(n):
        
        # 해당 문자 자체가 이미 숫자일 때 
        if s[i].isdigit():
            
            # 이전까지 입력된 단어를 숫자 변환 후 추가
            if temp:
                answer += num_dict[temp]
                temp =''     
            # 해당 숫자 문자 추가
            answer += s[i]
        
        # 해당 문자가 알파벳일 때
        else :
            # 해당 알파벳을 임시 객체에 추가
            temp += s[i]
            
            # 해당 알파벳까지 추가된 단어가 유의미할 때(숫자로 변환 가능)
            if temp in num_dict.keys():
                answer += num_dict[temp]
                temp = ''
            
            

    return int(answer)

