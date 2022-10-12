from time import time

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

def Solve(A):
    try:
        if not A[1]:
            pass
    except IndexError:
        return -1
    A = list(A)
    B = []
    for i in A:
        if i not in B:
            B.append(i)
    B.sort(reverse=True)
    return B[1]

 
A = [2] 
print(Solve(A))

# pass: solution

@calculate_time
def solve(A):
    try:
        if not A[1]:
            pass
    except IndexError:
        return -1
    A = list(A)
    import math
    max_no = -math.inf
    for i in A:
        if i > max_no:
            max_no = i
    max_no2 = -math.inf

    for i in A:
        if i>max_no2 and i != max_no:
            max_no2 = i
    
    return max_no2

@calculate_time
def Optimized_Solve(A):
    try:
        if not A[1]:
            pass
    except IndexError:
        return -1
    A = list(A)
    import math
    max_no = -math.inf
    second_max = 0
    for i in A:
        if i > max_no:
            second_max = max_no
            max_no = i
        if i > second_max and i != max_no:
            second_max = i
    return second_max

A= list(range(5))
A = [ 13, 7, 16, 18, 14, 17, 18, 8, 10 ]

print("Solve  =>" , solve(A))
print("Optimize =>" , Optimized_Solve(A))