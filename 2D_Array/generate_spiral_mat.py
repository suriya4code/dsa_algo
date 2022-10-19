	

def gen_element(A):
    for i in range(1,(A**2)+1):
        yield i

def generateMatrix(A):
    if A == 1:
        return [[1]]
    x = gen_element(A)
    N = A
    B = [[0 for i in range(A)] for j in range(A)]

    for k in range(int(N/2)+1): 
        i = j = k

        if N == 1:
            B[i][j] = x.__next__()

        for k in range(1,N):
            B[i][j] = x.__next__()
            j+=1

        for k in range(1,N):
            B[i][j] = x.__next__()
            i+=1
        for k in range(1,N):
            B[i][j] = x.__next__()
            j-=1
        for k in range(1,N):
            B[i][j] = x.__next__()
            i-=1
        N -=2
    return B

print(generateMatrix(21))
