import datetime

def solution(a,b):
    
    diff = 0
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    
    result = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    if a == 1:
        diff = b-1
        return result[diff%7]
    else :
        for i in range(1,a):
            diff += days[i]
        diff += b-1
        return result[diff%7]
    
# datetime.datetime(2016,a,b).weekday() # mon : 0