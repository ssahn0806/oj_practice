def solution(x,n):
    # x부터 시작해서 n개의 x배수를 갖는 리스트 반환
    answer = [x*(1+i) for i in range(n)]
    
    return answer