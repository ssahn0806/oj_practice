import math

def solution(a,b):
    return [math.gcd(a,b),a*b//math.gcd(a,b)]