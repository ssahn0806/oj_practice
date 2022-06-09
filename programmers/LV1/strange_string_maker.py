# 문자열 s는 한개 이상의 단어로 구성

# 각 단어는 하나 이상의 공백 문자로 구분

# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 반환

# 문자열 전체의 짝/홀수 인덱스가 아닌, 단어(공백을)별로 짝/홀수 인덱스를 판단해야함


# 첫번째 글자는 0번째 인덱스로 보아 짝수번째로 취급

def solution(s):
    
    result = ''
    idx = 0
    for val in s:
        if val.isalpha():
            if idx%2 == 0:
                result += val.upper()
            else :
                result += val.lower()
            idx +=1
        else :
            idx = 0
            result += val
    
    return result
        