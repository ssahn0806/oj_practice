def solution(m, n, board):
    
    # 1차원을 2차원으로 변경
    board = [
        list(board[i])
        for i in range(m)
    ]
    result = 0
    
    while True:
        exploit_board = [
        [0 for _ in range(n)]
        for _ in range(m)
        ]
        
        # 터질 위치 기록
        for i in range(m-1):
            for j in range(n-1):
                cnt = 0
                shape = board[i][j]

                if shape != '':
                    for k in range(2):
                        for l in range(2):
                            if board[i+k][j+l] == shape:
                                cnt+=1
                    if cnt == 4:
                        for k in range(2):
                            for l in range(2):
                                exploit_board[i+k][j+l] +=1
        
        # 터진 블록이 하나도 없으면 중단                        
        if sum([sum(row) for row in exploit_board]) == 0:
            return result
        
        # 터진 블록 수 업데이트   
        result += sum([1 for row in exploit_board for grid in row if grid>0])
        
        # 블록 떨어뜨리기
        for i in range(n):
            new_grid = []
            for j in range(m-1,-1,-1):
                if exploit_board[j][i]==0:
                    new_grid.append(board[j][i])
            while len(new_grid)<m:
                new_grid.append('')
            for j in range(m):
                board[j][i] = new_grid[m-j-1]