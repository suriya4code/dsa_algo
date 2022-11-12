A = [1, 2, 3]



def div_by_3(A):
    ans = 0
    for i in A:
        ans += i%3
    return 1 if ans%3==0 else 0

print(div_by_3(A))