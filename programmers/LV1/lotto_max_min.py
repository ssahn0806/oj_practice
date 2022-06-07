def solution(lottos,win_nums):
    
    # 현재 맞은 로또 번호 개수
    cur_cnt = sum(1 for num in lottos if num in win_nums)
    
    # 당첨 번호가 될 수 있는 개수
    zero_cnt = sum(1 for num in lottos if num == 0)
    
    # 최고 순위 : 현재 개수 + 0이 모두 당첨 번호
    max_th = 7 - (cur_cnt + zero_cnt)
    
    # 최저 순위 : 현재 개수
    min_th = 7 - cur_cnt
    
    # 최고,최저 순위가 6,7 이하인 경우 6순위로 통일
    max_th = 6 if max_th >= 6 else max_th
    min_th = 6 if min_th >= 6 else min_th
    
    return [max_th,min_th]