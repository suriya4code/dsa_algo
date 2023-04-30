def solve(A):
    if A == 1:
        print(1)
        return
    solve(A-1)
    print(A)

def solve2(A):
    if A == 1:
        return 1
    return (str(solve2(A-1)) + " "+ str(A))

import sys

print(sys.getrecursionlimit())
def solve3(A):
    if A == 1:
        print("1 ")
        return
    print(A,end=" ")
    solve3(A-1)

def print_asec(A):
        import sys
        sys.setrecursionlimit(10**6)
        if A == 1:
            print("1",end=" ")
            return
        print_asec(A-1)
        print(A,end=" ")

print_asec(999)