from time import time
import math

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        print("Starting time calculation")
        result = func(*args, **kwargs)
        print("Finished time calculation")
        end = time()
        print((end-start)*1000)
        return result
    return wrapper

@calculate_time
def Solve(A):
    result = []
    for i in range(1,A+1):
            digit_cube_sum = 0
            num = i
            while num>0:
                digit = num % 10
                digit_cube_sum += digit**3
                num //= 10
                
            if digit_cube_sum == i:
                    result.append(i)
    
    return result


@calculate_time
def IsArmstrong(i):
    digit_cube_sum = 0
    num = i
    while num>0:
        digit = num % 10
        digit_cube_sum += digit**3
        num //= 10
        
    if digit_cube_sum == i:
        print(i)
    
    return True



print("No of Armstrong numbers => ",Solve(153))