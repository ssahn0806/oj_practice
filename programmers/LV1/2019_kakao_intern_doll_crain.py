def find_pickup(board,col):
    
    # 뽑을 인형을 찾고, 뽑았다면 격자의 상태를 갱신도 진행함.
    n = len(board)
    for i in range(n):
        if board[i][col] == 0:
            continue
        result = board[i][col]
        board[i][col] = 0
        return result
    else :
        return 0
    
def solution(board,moves):
    
    # 뽑은 인형을 담을 스택
    result = []
    
    cnt = 0
    # 각 시도별로 집는 것을 시도하는 열의 위치
    for num in moves:
        # 집는 위치는 1부터 시작함에 유의!
        pickup_val = find_pickup(board,num-1)
        
        # 집을 대상이 있다면, 스택에 삽입
        if pickup_val != 0:
            result.append(pickup_val)
            
            # 스택에 비교대상이 있다면 비교 후 폭발 처리 및 카운팅
            if len(result)>=2 and result[-2] == result[-1]:
                cnt +=2
                result = result[:-2]
                # result.pop()
            
            
    return cnt

