st = 'abacbbabbcxyx'

def max_palindrome(A):
    result = 0
    max_len = 0
    for s in range(len(A)):
        for e in range(s+1,len(A)+1):
            st = A[s:e]
            if st == st[::-1]:
                l = e-s
                if l>max_len:
                    result = A[s:e]
                    max_len =  l
    
    return result

print(max_palindrome(st))



            
        