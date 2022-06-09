
def trinary(n):
    if n<=2:
        return str(n)
    return str(trinary(n//3)) + str(n%3)

def number(n):
    if len(n) == 1:
        return int(n)
    return 3**(len(n)-1)*int(n[0]) + int(number(n[1:]))
def solution(n):
    
    trinary_origin = trinary(n)
    trinary_reverse = trinary_origin[::-1]
    
    # int (num,i) : i진법으로 표현된 문자를 10진법 수로 변환함
    return int(trinary_reverse,3)
    # return number(trinary_reverse)
