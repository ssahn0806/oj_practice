def solution(board, skill):
    N = len(board)
    M = len(board[0])
    
    # 정확성만 통과하는 풀이
    '''
    diff = [
        [0 for _ in range(M)]
        for _ in range(N)
    ]
    
    for update in skill:
        t,r1,c1,r2,c2,deg = update
        
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                diff[i][j] += deg if t == 2 else -deg
    
    for i in range(N):
        for j in range(M):
            board[i][j] += diff[i][j]
    
    return sum(1 for row in board for cell in row if cell>=1)
    '''
    
    # 효율성도 통과하는 풀이
    diff = [
        [0 for _ in range(M+1)]
        for _ in range(N+1)
    ]
    
    # 누적합 테크닉
    for update in skill:
        t,r1,c1,r2,c2,deg = update
        
        diff[r1][c1] += deg if t == 2 else -deg
        diff[r1][c2+1] += -deg if t == 2 else deg
        diff[r2+1][c1] += -deg if t == 2 else deg
        diff[r2+1][c2+1] += deg if t == 2 else -deg
        
    for i in range(N+1):
        for j in range(1,M+1):
            diff[i][j] = diff[i][j-1] + diff[i][j]

    for i in range(M+1):
        for j in range(1,N+1):
            diff[j][i] = diff[j-1][i] + diff[j][i]
    
    # 최종 반영
    for i in range(N):
        for j in range(M):
            board[i][j] += diff[i][j]
    
    return sum(1 for row in board for cell in row if cell>=1)