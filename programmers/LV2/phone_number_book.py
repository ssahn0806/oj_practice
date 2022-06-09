def solution(phone_book):
    
    # 사전순으로 정렬하기
    phone_book.sort(key=lambda x: (x,len(x)))

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
#     phone_book.sort(key=len)
#     hash_table = {}
    
#     for number in phone_book:
#         for key in hash_table:
#             if number.startswith(key):
#                 hash_table[key].append(number)
#                 return False
#         hash_table[number] = []
            
    return True

'''
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
'''