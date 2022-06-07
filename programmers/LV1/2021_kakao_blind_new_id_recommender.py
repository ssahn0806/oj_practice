def solution(new_id):
    
    # step 1 : 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # step 2 : 소문자, 숫자, -, _, . 이외 제거
    temp_id = ''
    for st in new_id:
        if st.islower() or st.isdigit() or st in ['-','_','.']:
            temp_id += st
    
    # step 3 : .가 2번 이상 연속하는 경우 하나로 치환
    new_id = ''
    cnt = 0
    for i in range(len(temp_id)):
        if temp_id[i] == '.':
            cnt+=1
        else :
            if cnt>0:
                new_id += '.'
                cnt = 0
            new_id += temp_id[i]
            
    # step 4 : .가 처음과 끝에 위치하는 경우 제거    
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
            
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # step 5 : 빈 문자열이라면 a 대입
    if not new_id:
        new_id = 'a'
    
    # step 6 : 문자열 길이가 16자 이상인 경우, 첫 15개 이후 제거 후 마지막 문자가 .이라면 추가 제거
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # step 7 : 2글자 이하라면 3글자가 될때까지 마지막 문자 반복 삽입
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id += new_id[-1]
    
    return new_id