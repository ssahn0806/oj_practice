import re
from itertools import product


def solution(user_id, banned_id):
    
    n = len(banned_id)
    # 각 제재 가능성을 정규식으로 변환한 배열
    banned_regex = ['']*n
    
    # 긱 정규식별로 가능한 사용자 후보 목록
    # banned_cadidates = [[] for _ in range(n)]
    
    # 최종 제재 목록 집합(중복 허용하지 않음, 순서 무관)
    result = []

    for idx,keyword in enumerate(banned_id):
        search = ''
        for c in keyword:
            if c.isalpha() or c.isdigit():
                search+=c
            else :
                search+="[a-z0-9]"
        banned_regex[idx] = search
    
    '''
    # 각 정규식 배열과 일치하는 사용자를 추출    
    for idx,regex in enumerate(banned_regex):
        for id in user_id:
            p = re.fullmatch(regex,id)
            if p != None:
                banned_cadidates[idx].append(p.group())
    result = set()
    
    temp = set(product(*banned_cadidates))

    for item in temp:
        if len(set(item)) == n:
            result.add(tuple(set(item)))
            
    return len(result)
    '''
                
    banned_candidates = ([i for i,id in enumerate(user_id) if re.fullmatch(regex,id)] for regex in banned_regex)
    
    result = (set(id) for id in product(*banned_candidates))
    
    
    result = set(tuple(id) for id in result if len(id) == n)
    
            
    return len(result)