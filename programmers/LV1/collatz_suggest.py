def solution(num):
    cnt = 0
    
    while cnt<=500:
        if num == 1:
            return cnt
        cnt+=1
        num = num//2 if num%2==0 else num*3 + 1
        

    else :
        return -1
    