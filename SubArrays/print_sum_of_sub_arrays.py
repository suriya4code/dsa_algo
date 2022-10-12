


A = [2,3,4,5,6,7]


def sum_of_Subarray(A, s, e):
    sum_of = 0
    for i in range(s,e+1):
        sum_of += A[i]
    return sum_of

def print_sum_of_all_SubArray(A):
    sum_of = 0
    for s in range(len(A)):
        for e in range(s,len(A)):
            sum_of += sum_of_Subarray(A, s, e)
    return sum_of


print(print_sum_of_all_SubArray(A))

#Using Prefix Sum
def sum_of_Subarrays(A):
    #preffix sum
    ps = []
    ps.append(A[0])
    sum_of = 0

    for i in range(1,len(A)):
        ps.append(ps[i-1]  + A[i])
    for s in range(len(A)):
        for e in range(s,len(A)):   
            sum_of += (ps[e]-ps[s-1])
    return sum_of


print(sum_of_Subarrays(A))

def optimized_approach(A):
    
    for s in range(len(A)):
        sum_of = 0
        for e in range(s,len(A)):   
            sum_of += A[e]
            print(sum_of)


# print(optimized_approach(A))

def optimized_approach2(A):
    sum_of = 0
    for s in range(len(A)):
        for e in range(s,len(A)):   
            sum_of += A[e]
    return sum_of

print(optimized_approach2(A)) 

#O(N) Solution

def O_N_solution(A):
    sum_of = 0
    for i in range(len(A)):
        x = i+1
        y = len(A)-i
        sum_of += A[i]*x*y
    return sum_of
print(O_N_solution(A))