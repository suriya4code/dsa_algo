 
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

def solve(self, A):
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
