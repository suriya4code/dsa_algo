A = "aAbBcC"

def togglrStr(A):
    b = []
    for i in range(len(A)):
        if A[i].isupper():
            b.append(A[i].lower())
        else: b.append(A[i].upper())
    return "".join(b)
    # for i in range(0, len(A)):
    #     A[i]^=32
    # return A

print(togglrStr(A))