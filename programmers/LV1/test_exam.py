from collections import deque

def solution(answers):
    
    # 각 사람이 찍는 순서 큐
    p1 = deque([1,2,3,4,5])
    p2 = deque([2,1,2,3,2,4,2,5])
    p3 = deque([3,3,1,1,2,2,4,4,5,5])
    
    # 각 사람이 맞춘 문제 수
    cnt = [0,0,0]
    
    # 정답
    answer = []
    
    # 각 문제의 정답에 대하여, 각 사람이 찍은 값과 비교 후 정답일 시 카운트
    for ans in answers:
        r1 = p1.popleft()
        r2 = p2.popleft()
        r3 = p3.popleft()
        
        if r1 == ans:
            cnt[0]+=1
        if r2 == ans:
            cnt[1]+=1
        if r3 == ans:
            cnt[2]+=1
        p1.append(r1)
        p2.append(r2)
        p3.append(r3)
    
    # 각 사람의 카운트 중 최댓값 찾기
    max_v = max(cnt)
    
    # 각 사람의 카운트가 최댓값과 같은 경우 리스트에 추가
    for idx,c in enumerate(cnt):
        if c == max_v:
            answer.append(idx+1)
        
    return answer