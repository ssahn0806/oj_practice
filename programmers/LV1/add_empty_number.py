def solution(numbers):
    
    # 각 숫자의 개수를 카운팅
    
    num_cnt = [0]*10
    
    # 정답
    answer = 0
    
    # 숫자 배열을 순회하며 각 숫자의 개수를 갱신
    for num in numbers:
        num_cnt[num]+=1
    
    # 각 숫자 개수가 0인 경우 해당 인덱스(숫자)를 추가
    for idx,val in enumerate(num_cnt):
        if val == 0:
            answer += idx
    
    return answer