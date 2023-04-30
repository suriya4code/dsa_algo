A = "madam"

def check_palindrome(A):
    A = str(A)
    n = len(A)
    if n == 0 or n == 1:
        return 1
    if A[0] == A[n-1]:
        return check_palindrome(A[1:n-1])
    else:
        return 0

print(check_palindrome(A))