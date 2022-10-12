A = [2,3,4,5,6,7]
s = 3
e = 5

def printSubArray(A, s, e):
    a = []
    for i in range(s,e+1):
        a.append(A[i])
    print(a)


def print_all_SubArray(A):
    for s in range(len(A)):
        for e in range(s,len(A)):
            printSubArray(A,s,e)

print_all_SubArray(A)

 