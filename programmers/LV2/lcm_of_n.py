import math

# math.lcm 사용 불가.
# math.gcm : 두개의 수에 대해서만 결과를 얻을 수 있음.

# 두 수의 최소 공배수 : 최대 공약수 x 두 수를 최대공약수로 나눈 몫
# 두 수의 곱을 최대 공약수로 나눈 값

def solution(arr):
    n = len(arr)
    answer = arr[0]

    for i in range(1,n):
        GCD = math.gcd(answer,arr[i])
        LCM = answer*arr[i]//GCD
        answer = LCM
    return answer