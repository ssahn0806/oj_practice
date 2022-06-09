import sys

def solution(land):

    N = len(land)
    
    dp_table = [
        [0 for _ in range(4)]
        for _ in range(N)
    ]
    
    # dp_table[i][j] : (i행에서 j열을 선택했을 때까지 얻은 최대 점수)
    
    for i in range(4):
        dp_table[0][i] = land[0][i]
    
    for i in range(1,N):
        for j in range(4):
            prev_max = max([dp_table[i-1][k] for k in range(4) if k!=j])
            dp_table[i][j] = prev_max + land[i][j]
    
    return max(dp_table[N-1])