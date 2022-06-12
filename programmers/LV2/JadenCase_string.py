def solution(s):
    # 모두 소문자로 바꾼 뒤에 처리하자(숫자가 들어있어도 오류가 나지 않음)
    s = s.lower()
    
    result = ''
    idx = 0
    
    for c in s:
        # 단어의 첫 위치인 경우
        if idx == 0:
            # 알파벳인 경우
            if c.isalpha():
                result += c.upper()
                idx+=1
            # 알파벳이 아닌 숫자인 경우
            elif c.isdigit():
                result += c
                idx+=1
            # 공백이 연속된 경우
            else :
                result += c
        # 그 외의 위치인 경우        
        else :
            result += c
            
            # 공백이 등장한다면 해당 단어가 끝났음을 체크
            if c == ' ':
                idx = 0
            else :
                idx +=1
    return result
                
        