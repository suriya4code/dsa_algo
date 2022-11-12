from time import time

start = time()
N = 2
M = 3
Q = 4


B = ["1 2 3","3 1 2 2 2","2 1 2","4 1 2 2 3"]


#gen build
def gen_mat(l):
    for i in range(1,l+1):
        yield i

#mat build
Mat = [[0 for i in range(M)] for i in range(N)]
x = gen_mat(N*M)
for i in range(N):
    for j in range(M):
        Mat[i][j] = x.__next__()

def row_swap(mat,r1,r2):
    r1 -=1
    r2 -=1
    mat[r1],mat[r2] = mat[r2],mat[r1]
    return mat 
def col_swap(mat,c1,c2):
    c1 -=1
    c2 -=1
    for i in range(N):
        mat[i][c1],mat[i][c2] = mat[i][c2],mat[i][c1]
    return mat

def check_bit_and(mat,a,b,c,d):
    a-=1
    b-=1
    c-=1
    d-=1
    print(mat[a][b] & mat[c][d])

def check_bit_or(mat,a,b,c,d):
    a-=1
    b-=1
    c-=1
    d-=1
    print(mat[a][b] | mat[c][d])

#check query parameters
for i in B:
    if i.startswith("1"):
        i_lst = i.split()
        Mat = col_swap(Mat,int(i_lst[1]),int(i_lst[2]))
    elif i.startswith("2"):
        i_lst = i.split()
        Mat = row_swap(Mat,int(i_lst[1]),int(i_lst[2]))
    elif i.startswith("3"):
        i_lst = i.split()
        check_bit_or(Mat,int(i_lst[1]),int(i_lst[2]),int(i_lst[3]),int(i_lst[4]))
    elif i.startswith("4"):
        i_lst = i.split()
        check_bit_and(Mat,int(i_lst[1]),int(i_lst[2]),int(i_lst[3]),int(i_lst[4]))
# print(Mat)
end = time()
print((end-start)*1000)