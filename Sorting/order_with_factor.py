A = [6, 8, 9]
A = [ 36, 13, 13, 26, 37, 28, 27, 43, 7 ]


def factors_count(B):

    count = 0
    for i in range(1,B+1):
        if i*i==B:
            count += 1
            continue
        if i > B/i:
            return count
        if B%i == 0:
            count += 2
    
    return count

def solve(A):
    # return sorted(A, key=lambda ele: len(
    #     [ele for idx in range(1, ele) if ele % idx == 0]))
    A.sort()
    A.sort(key=factors_count)
    return A

print(solve(A))

