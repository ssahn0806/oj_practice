from math import ceil

class Car():
    def __init__(self,time):
        self.state = 1
        self.in_time = time
        self.total_time = 0
        self.total_fee = 0
        
    def calc_time(self,in_time,out_time):
        iH,iM = map(int,in_time.split(":"))
        oH,oM = map(int,out_time.split(":"))
        
        self.total_time += (oH-iH-1 if oH>iH else 0)*60 + (oM-iM if oH == iH else (60-iM)+oM)
    
    def get_time(self):
        return self.total_time 
    
    def set_fee(self,fee):
        self.total_fee = fee
    
    def get_fee(self):
        return self.total_fee
        
    def park_in(self,time):
        self.in_time = time
        self.state = 1
        
    def go_out(self,time):
        self.calc_time(self.in_time,time)
        self.state = 0
        
    def is_parking(self):
        return self.state == 1
        
    def force_out(self):
        if self.is_parking():
            self.go_out("23:59")
        
def solution(fees, records):
    
    car_dict = {}
    std_min,std_fee,add_min,add_fee = fees
    
    def calc_fee(target_min):
        result = std_fee
        
        if target_min > std_min:
            rest_min = target_min-std_min
            temp = ceil(rest_min/add_min)*add_fee
            result += temp
        
        return result
            
    for record in records:
        time, number, state = record.split()
        if state == "IN":
            if number not in car_dict.keys():
                car_dict[number] = Car(time)
            else :
                car_dict[number].park_in(time)
        else :
            car_dict[number].go_out(time)
    
    for car in car_dict.values():
        car.force_out()
        car.set_fee(calc_fee(car.get_time()))
        
    result_arr = sorted(car_dict.items(),key=lambda x:x[0])
    answer = [car.get_fee() for _,car in result_arr]
    return answer
        
        
        
# print(solution([180,5000,10,600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# print(solution([1, 461, 1, 10]	,["00:00 1234 IN"]))


