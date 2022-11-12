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



def is_prime(A):
    prime = True
    for i in range(2,A//2):
        if A%i == 0:
            prime = False
            break
    return prime

A = 5
B = 20**2
index = "odd"

@calculate_time
def solve(A,B,index):
    p = []
    for i in range(A,B+1):
        if is_prime(i): p.append(i)
    return p[::2] if index == "even" else p[1::2]

print(solve(A,B,index))
