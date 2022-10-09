from time import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        print("Starting time calculation")
        result = func(*args, **kwargs)
        print("Finished time calculation")
        end = time()
        print((end-start)*1000)
        return result
    return wrapper


# @calculate_time
# def sum_of_L_R(A, B):
#     result = []
#     for i in B:
#         count = 0
#         for j in range(i[0],i[1]+1):
#             if A[j]%2==0:
#                 count  += 1
#         result.append(count)
#     return result

@calculate_time
def Optimize(A, B):
    ps = [0]* len(A)
    for i in range(len(A)):
        if A[i]%2==0:
            ps[i] = ps[i-1] + 1
        else:
            ps[i] = ps[i-1]
    print(ps)
    result = [0] * len(B)
    for i in range(len(B)):
        if B[i][0]==0:
            result[i] = ps[B[i][1]]
        else:
            result[i] = ps[B[i][1]] - ps[B[i][0]-1]

    return result
        



@calculate_time
def sum_of_L_R(A, B):
    # print(A)
    for i in range(len(A)):
        if A[i]%2  == 0:
            A[i] = 1
        else:
            A[i] = 0
    ps = []
    ps.append(A[0])
    for j in range(1,len(A)):
        ps.append(A[j] + ps[j-1])
    # ps[start, end] = ps[end] - ps[start-1]
    # print(A)
    print(ps)
    result = []
    for j in B:
        start = j[0]
        end = j[1]
        if start == 0:
            val = ps[end]
        else:
            # print(ps[end], ps[start-1])
            val = ps[end] - ps[start-1]

        result.append(val)
    return result

@calculate_time
def solve(A, B):
    n = len(A)
    pref = [0] * (n + 1)
    print(pref)
    for i in range(n):
        if A[i] % 2 == 0:
            pref[i + 1] = pref[i] + 1
        else:
            pref[i + 1] = pref[i]
    ans = [0] * len(B)
    print(pref)
    for i in range(len(B)):
        ans[i] = pref[B[i][1] + 1] - pref[B[i][0]]
    return ans

# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [2, 3],[1,4]]

# A = [2, 2, 2]
# B = [[1, 1], [2, 3]]
A = [ 6, 3, 3, 6, 7, 8, 7, 3, 7 ]
B = [[2, 6],[4, 7],[6, 7]]

A = [ 3, 1, 5, 7, 5, 2 ]
B = [[0, 2]]

# print(sum_of_L_R(A, B))
print(solve(A, B))
print(Optimize(A, B))