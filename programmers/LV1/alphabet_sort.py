def solution(s):
    s = list(s.swapcase())
    s.sort(reverse=True)
    s = [i.swapcase() for i in s]
    s.sort(reverse=True)
    return ''.join(s)
