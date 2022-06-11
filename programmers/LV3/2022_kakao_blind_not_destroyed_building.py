def solution(board, skill):
    N = len(board)
    M = len(board[0])
    
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