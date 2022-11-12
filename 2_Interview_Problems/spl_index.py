import copy


A=[1,2,3,4,5]
A = [ 1, 2, 3, 7, 1, 2, 3 ]
# A=[2, 1, 6, 4]

def solve(A):
    import copy
    count = 0
    for k in range(len(A)):
        B = copy.deepcopy(A)
        B.remove(A[k])

        N = len(B)
        res = []
        pse = []
        pse.append(B[0])
        for i in range(1,N):
            if i % 2 != 0:
                pse.append(pse[i-1])
            else:
                pse.append(pse[i-1]+B[i])
        pso = []
        pso.append(0)
        for j in range(1,N):
            if j % 2 == 0:
                pso.append(pso[j-1])
            else:
                pso.append(pso[j-1]+B[j])
        if pse[-1] == pso[-1]:
                count += 1
    return count

def solve2(A):
        count = 0
        N = len(A)
        res = []
        pse = []
        pse.append(A[0])
        for i in range(1,N):
            if i % 2 != 0:
                pse.append(pse[i-1])
            else:
                pse.append(pse[i-1]+A[i])
        pso = []
        pso.append(0)
        for j in range(1,N):
            if j % 2 == 0:
                pso.append(pso[j-1])
            else:
                pso.append(pso[j-1]+A[j])
       
        for k in range(N):
            if k == 0:
                sum_odd = pse[N-1]-pse[k]
                sum_even = pso[N-1]
            elif k == N-1:
                sum_odd = pso[k-1]
                sum_even = pse[k-1]
            else:
                sum_odd = pso[k-1] + pse[N-1]-pse[k]
                sum_even = pse[k-1] + pso[N-1]-pso[k]
            if sum_odd == sum_even:
                count += 1

        return count
            
            
            




print(solve(A))
print(solve2(A))