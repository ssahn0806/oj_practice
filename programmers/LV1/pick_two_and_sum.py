def solution(numbers):
    
    # 배열의 길이
    n = len(numbers)
    
    # 중복된 값을 제거한 합을 저장할 객체
    sum_set = set()
    
    # O(N^2)
    for i in range(n):
        for j in range(i+1,n):
            # 서로 다른 인덱스의 값을 합하여 객체에 추가
            sum_set.add(numbers[i]+numbers[j])
    
    # 정렬된 리스트로 결과 반환
    result = sorted(sum_set)
    
    return result