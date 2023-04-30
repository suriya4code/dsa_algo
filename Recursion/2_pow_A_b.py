#pow(a,n)

def pow_a(a,n):
    if n==1: return 1
    return a * pow_a(a,n-1)

def pow_a_2(a,n):
    if n==0: return 1
    halfpow = pow_a_2(a,n//2)
    halfAns = halfpow * halfpow
    if n % 2 == 0: return halfAns
    else: return halfAns * a

# print(pow_a_2(4,2))

def pow_a_n_d(a, n, d):
    if n==0: return 1
    halfpow = pow_a_n_d(a,n//2,d)
    halfAns = (halfpow %d) * (halfpow %d)
    if n % 2 == 0: return halfAns %d
    else: return (halfAns %d) * (a %d)

# print(pow_a_n_d(10,4,2))

def pow_a_n_d(A, B, C):
    if B==0: return 1
    halfpow = pow_a_n_d(A,B//2,C)
    halfAns = (halfpow %C) * (halfpow %C)
    if B % 2 == 0: return halfAns %C
    else: return (halfAns %C) * (A %C)


def pow_d(A, B, C):
    import sys
    sys.setrecursionlimit(10**6)
    if A==0: return 0
    if B==0: return 1
    halfpow = pow_d(A,B/2,C)
    halfAns = ((halfpow %C) * (halfpow %C)) %C
    if B % 2 == 0: return halfAns %C
    else: return ((halfAns %C) * (A %C)) %C

A = 71045970
B = 41535484
C = 64735492
print(pow_d(A, B, C))