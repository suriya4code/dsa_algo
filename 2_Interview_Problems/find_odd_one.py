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




A = [ 723, 256, 668, 723, 140, 360, 597, 233, 128, 845, 737, 804, 986, 701, 906, 512, 845, 510, 510, 227, 430, 701, 366, 946, 464, 619, 946, 627, 209, 771, 424, 555, 959, 711, 530, 937, 716, 261, 505, 658, 706, 140, 511, 277, 396, 233, 819, 196, 475, 906, 583, 261, 147, 658, 517, 197, 196, 702, 944, 711, 128, 555, 149, 483, 530, 291, 716, 258, 430, 464, 601, 749, 149, 415, 802, 573, 627, 771, 660, 601, 360, 986, 291, 51, 415, 51, 227, 258, 937, 366, 923, 669, 33, 517, 417, 702, 475, 706, 110, 417, 275, 804, 500, 473, 746, 973, 669, 275, 973, 147, 817, 657, 277, 923, 144, 660, 197, 511, 793, 893, 944, 505, 322, 817, 586, 512, 322, 668, 33, 424, 962, 597, 144, 746, 345, 753, 345, 269, 819, 483, 368, 802, 573, 962, 583, 615, 208, 209, 269, 749, 256, 657, 619, 893, 959, 473, 753, 299, 396, 299, 500, 368, 586, 110, 793, 737, 615 ]
# A = [ 32, 34, 32, 725, 659, 980, 273, 725, 286, 875, 273, 538, 875, 34, 931, 150, 124, 150, 931, 659, 286, 124, 538 ]

@calculate_time
def singleNumber(A):
    N = len(A)
    A = list(A)
    A.sort()
    # print(A)
    for i in range(0,N,2):
        if i==N-1:
            return A[i]

        if A[i] != A[i+1]:
            return A[i]

@calculate_time        
def singleNumber_sln(A):
    ret = A[0]
    for i in range(1, len(A)):
        # xor of all the elements of the array
        ret ^= A[i]
    return ret        

print(singleNumber(A))
print(singleNumber_sln(A))