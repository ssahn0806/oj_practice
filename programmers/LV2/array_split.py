def solution(n, left, right):
    ''' 시간 초과
    # STEP 1
    grid = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    # STEP 2
    for i in range(n):
        for j in range(n):
            grid[i][j] = max(i+1,j+1)

    # STEP 3
    arr = [val for row in grid for val in row]

    # STEP 4
    return arr[left:right+1]
    '''

    # STEP 2,3,4를 한번에 처리
    return [max(i//n+1,i%n+1) for i in range(left,right+1)]