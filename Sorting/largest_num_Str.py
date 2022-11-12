
A = [3, 30, 34, 5, 9]

def largestNumber(A):
    A = list(A)
    def mod(i):
        return i%10
    A.sort(reverse=True,key=mod)
    res = ""
    for i in A:
        res += str(i)
    return res

print(largestNumber(A))