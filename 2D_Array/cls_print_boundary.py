# A = [[1,2,3,4],[5,6,7,8],[9,2,3,4],[1,2,3,4]]
A = [[1,2,3],[4,5,6],[7,8,9]]



def print_boundary_elem(A,N,i,j):

    if N < 2:
        print(A[i][j])

    for k in range(1,N):
        print(A[i][j])
        j+=1
    for k in range(1,N):
            print(A[i][j])
            i+=1
    for k in range(1,N):
            print(A[i][j])
            j-=1
    for k in range(1,N):
            print(A[i][j])
            i-=1

def spiral_printing(A,N):
    for k in range(int(N/2)+1):
        print_boundary_elem(A,N,k,k)
        N -=2




# print_boundary_elem(A,4,0,0)
spiral_printing(A,len(A))