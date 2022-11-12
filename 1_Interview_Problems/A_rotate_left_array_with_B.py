A = [1, 2, 3, 4, 5]
B = [2, 3, 6]
A = [5, 17, 100, 11]
B = [5]
# A : [ 1, 2, 3, 4, 5 ]
# B : [ 2, 3 ]
# A = [ 4, 74, 35, 16, 100, 77, 50, 51, 31, 29, 67, 12, 43, 31, 83, 2, 85, 85, 39, 27, 64, 86, 5 ]
# B = [ 73, 70, 47, 19, 46, 25, 46, 4, 33, 33, 6, 31, 23, 19, 44, 53, 69, 30, 69, 89, 59, 25, 38, 82, 26, 8, 36, 3 ]

# A = [ 6, 31, 33, 13, 82, 66, 9, 12, 69, 21, 17, 2, 50, 69, 90, 71, 31, 1, 13, 70, 94, 46, 89, 13, 55, 54, 67, 97, 28, 27, 62, 34, 41, 18, 15, 35, 13, 84, 93, 27, 89, 23, 6, 56, 94, 40, 54, 95, 47 ]
# B = [ 88, 85, 98, 36, 66, 40, 30, 26, 51, 77, 62, 60, 92, 64, 53, 86, 24, 53, 85, 49, 57, 29, 32, 60, 75, 82, 17, 23, 67, 51, 23, 11, 70, 59 ]

def reverse(arr,i,j):
    start = i
    end = j

    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

    return arr


# @calculate_time
def left_rotate(arr,k):
    N = len(A)
    if k > N:
        k = k%N
    if k == N:
        return arr
    r1 = reverse(arr,0,N-1)
    r2 = reverse(r1,0,N-k-1)
    r3 = reverse(r2,N-k,N-1)

    return r3
    
def solve(A,B):
    import copy
    res = [copy.deepcopy(A) for i in range(len(B))]
    for i in range(len(B)):
        res[i] = left_rotate(res[i],B[i])
    return res  


def solve2(A, B):
    ans = []
    for i in range(len(B)):
        temp = []
        ind = B[i]%len(A)
        for j in range(ind, len(A)): 
            temp.append(A[j])
        for j in range(ind):
            temp.append(A[j])
        ans.append(temp);
    
        return ans
print("Reversed array => ",solve(A,B))
print("Reversed array => ",solve2(A,B))