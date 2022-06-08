def solution(n,arr1,arr2):
    # nxn, 공백 또는 벽(#)
    # 두장의 지도를 겹쳐서 얻음 (둘중 하나라도 벽이면 벽, 둘 다 공백이면 빈공간) : 비트 연산 (OR)
    # 두장의 지도는 정수 배열로 암호화 (이진수 벽 :1 , 빈공간 : 0)
    
    result = []
    grid1 = []
    
    grid2 = []
    
    bits = [2**i for i in range(n-1,-1,-1)]
    
    for num in arr1:
        # 십진수는 n비트 2진수로 필쳐야함.
        # temp = bin(num)[2:]
        
        # rjust, ljust (num,str) : 해당 방향으로 정렬한뒤 빈공간을 해당 문자로 채운다. zfill (num) : 0을 왼쪽에 자릿수에 맞게 채움
        # replace(str1,str2) : str1을 str2로 교체한다.
        
        temp = ''
        for bit in bits:
            temp += ('#' if num//bit else ' ')
            num%=bit
        
        grid1.append(temp)
        
    for num in arr2:
        # 십진수는 n비트 2진수로 필쳐야함.
        temp = ''
        for bit in bits:
            temp += ('#' if num//bit else ' ')
            num%=bit
        
        grid2.append(temp)
    
    for row1,row2 in zip(grid1,grid2):
        temp = ''
        for i,j in zip(row1,row2):
            temp += (' ' if i == ' ' and j == ' ' else '#')
        result.append(temp)
    
    return result
            
        