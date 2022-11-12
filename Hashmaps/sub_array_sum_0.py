# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.

A = [1, 2, 3, 4, 5]
A = [ 1, -1 ]

def solve(A):
    n = len(A)

    if A[0]==0:
        return 1

    ps = []
    ps.append(A[0])

    for i in range(1,n):
        if A[i] == 0 or (ps[i-1]+A[i]) == 0:
            return 1
        
        ps.append(ps[i-1]+A[i])

    for s in range(n):
        sum_of = 0
        for e in range(s,n):
            if s==0:
                sum_of = ps[e]
            else:
                sum_of = ps[e] - ps[s-1]
            if sum_of == 0:
                return 1
    return 0
        


print(solve(A))


def solve2(A):
    n = len(A)
    if A[0]==0:
        return 1

    ps = []
    ps.append(A[0])
    
    for i in range(1,n):
        if A[i] == 0:
            return 1
        pse = (ps[i-1]+A[i])

        if pse == 0:
            return 1
        
        if ps.get(pse)!=None:
            return 1

        ps.append(ps[i-1]+A[i])
    return 0

print(solve2(A))
