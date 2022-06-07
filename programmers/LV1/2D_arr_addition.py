def solution(arr1,arr2):
    
    row = len(arr1)
    col = len(arr1[0])
    result = [
        [0 for _ in range(col)]        
        for _ in range(row)
    ]
    
    for i in range(row):
        for j in range(col):
            result[i][j] = arr1[i][j] + arr2[i][j]
            
    return result