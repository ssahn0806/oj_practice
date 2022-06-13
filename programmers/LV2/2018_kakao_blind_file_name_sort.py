def find_number_start_idx(file):
    for idx,i in enumerate(file):
        if i.isdigit():
            return idx

def find_tail_start_idx(file,num_start_idx):
    for idx,i in enumerate(file[num_start_idx+1:]):
        if idx>=4:
            return num_start_idx+5
        if not i.isdigit():
            return num_start_idx+idx+1
        
def solution(files):
    answers = [tuple()]*len(files)
    
    for idx,file in enumerate(files):
        head,number = 0,find_number_start_idx(file)
        tail = find_tail_start_idx(file,number) # [None:] -> [:] 와 동일한 결과
        answers[idx] = (file[:number],file[number:tail],'' if tail == None else file[tail:],idx)
    
    answers.sort(key = lambda x : (x[0].lower(), int(x[1]), x[3]))
    
    answers = [''.join(map(str,answer[:-1])) for answer in answers]
    return answers


# 파일명 : 100글자 이내 (영문 대소문자,숫자,공백,마침표,뺴기부호, 영문자로 시작하며 숫자는 하나이상 포함)
# HEAD, NUMBER, TAIL

# HEAD : 숫자가 아닌 문자(최소 한글자 이상)
# NUMBER : 한글자에서 최대 다섯 글자인 연속된 숫자(앞쪽에 0가능) 
# TAIL : 나머지 부분 (숫자도 가능,아무 글자가 없을수도 있음)

# 1차 : HEAD 기준 사전순으로 정렬(대소문자는 구분하지 않음)
# 2차 : 숫자 오름차순으로 정렬 (0으로 시작되는 부분은 무시, 012 == 12)
# 3차 : 원래 입력 순서 유지 


