import numpy as np

def solution(arr1, arr2):
    
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    
    np_mul = np_arr1.dot(np_arr2)
    
    answer = np_mul.tolist() 
    # answer = [[]]
    return answer