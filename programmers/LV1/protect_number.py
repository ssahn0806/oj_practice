def solution(phone_number):
    # 맨뒤 4자리 제외 갯수 만큼 * 처리, 마지막 4자리 이어붙이기
    return '*'*len(phone_number[:-4]) + phone_number[-4:] 