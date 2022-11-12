A = "scaler"
B = [[0,2],[2,4]]

def solve(A,B):
    vowels = ["a","e","i","o","u"]
    count = 0
    res = []
    v_s = []
    count =1 if A[0] in vowels else 0
    v_s.append(count)
    for i in range(1, len(A)):
        if A[i] in vowels: count += 1
        v_s.append(count)
    for j in B:
        start = j[0]
        end = j[1]
        if start==0:
            count_vow = v_s[end]
        else:
            count_vow = v_s[end]-v_s[start-1]
        res.append(count_vow)
    return res

        
    

print(solve(A,B))




# A = "scaler"
# B = [[0,2],[2,4]]

# def solve(A,B):
#     pass

# print(A,B)