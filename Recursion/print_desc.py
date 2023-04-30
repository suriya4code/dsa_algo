import sys
sys.setrecursionlimit(10**6)
def printAto1(A):
    if(A == 0):
        return
    printAto1(A - 1)
    print(A, end = " ")

def solve(A):
    printAto1(A)
    print()

solve(5)