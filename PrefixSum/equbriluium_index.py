# You are given an array A of integers of size N.

# Your task is to find the equilibrium index of the given array

# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

# NOTE:

# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.

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

def find_ps_value(ps, index):
    return ps[index]

def find_Equ_index(A):
    #prefix sum array
    ps = []
    ps.append(A[0])
    for j in range(1,len(A)):
        ps.append(A[j] + ps[j-1])
    
    print(f" Prefix sum array = > {ps}")
    equ_index = []
    for i in range(len(A)):
        sum_left = 0
        sum_right = 0
        if i == 0:
            sum_left = 0
            sum_right = ps[-1]-A[0]
        else:
            sum_left = ps[i-1]
            sum_right = ps[-1] - A[i] - sum_left
        
        print(f'Checking whether {sum_left} == {sum_right}')
        if sum_right == sum_left:
            equ_index.append(i)
    equ_index.sort()

    return equ_index[0] if len(equ_index) > 0 else -1
    
        


        
A = [ 1, 2, 3, 7, 1, 2, 3 ]
# A = [1,2,9,3]
# B = [[1, 4], [2, 3],[1,5]]

# A = [2, 2, 2]
# B = [[1, 1], [2, 3]]

print(find_Equ_index(A))
