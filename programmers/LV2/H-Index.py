def solution(citations):
    #     n = len(citations)
#     answer = min(citations)
    
#     for i in range(min(citations)+1,n):
#         result = [0]*n
#         # i번 이상 인용된 논문 찾기
#         for j in range(n):
#             if citations[j]>=i:
#                 result[j] = 1
#         # 인용 논문 개수 체크
#         if sum(result) >= i:
#             # 나머지 논문 인덱스 구하기
#             cit2 = [idx for idx,val in enumerate(result) if val == 0]
            
#             can_update = True
#             for i in cit2:
#                 if citations[i]>i:
#                     can_update = False
#                     break
            
#             if can_update:
#                 answer = i
#             # if sum([citations[idx] for idx in cit2])<=i:
#             #     answer = i
    
    citations.sort(reverse=True)
    
    answer = 0
    for idx,val in enumerate(citations):
        if idx<val:
            continue
        answer = idx
        break
    
    if answer == 0 and citations[0]!=0:
        answer = len(citations)
    return answer