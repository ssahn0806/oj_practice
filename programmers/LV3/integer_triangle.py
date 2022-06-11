def solution(triangle):
    
    height = len(triangle)
    
    if height == 1:
        return triangle[0][0]
    
    if height == 2:
        return max(triangle[0][0]+triangle[1][0],triangle[0][0],triangle[1][1])
    
    dp_table = [
        [-1]*(i+1)
        for i in range(height)
    ]
    
    # dp[i][j] : i,j까지 도달했을 때 거쳐간 숫자의 합의 최대를 저장
    
    dp_table[0][0] = triangle[0][0]
    dp_table[1][1] = dp_table[0][0] + triangle[1][1]
    
    # 맨 첫항은 위에서 내려오는 경우 밖에 없음
    for i in range(1,height):
        dp_table[i][0] = dp_table[i-1][0] + triangle[i][0]
    
    for i in range(2,height):
        for j in range(1,i):
            # 그 외에는 두개의 값 중 더 큰값을 택해야 함.
            dp_table[i][j] = max(dp_table[i-1][j-1],dp_table[i-1][j]) + triangle[i][j]
            
        # 맨 끝항은 왼쪽 위 대각선에서 내려오는 경우 밖에 없음
        dp_table[i][i] = dp_table[i-1][i-1] + triangle[i][i]
            

    return max(dp_table[height-1])

