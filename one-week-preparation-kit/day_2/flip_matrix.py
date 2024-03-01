matrix = [[112,42, 83, 119], [56, 125,56,49], [15,78,101,43], [62, 98,114,108]]
def print_matrix(mat): 
    for i in mat:
        print(i)
print_matrix(matrix)

n = int(len(matrix[0])/2)
s = 0
for i in range(n):
    for j in range(n):
        # i,j =0,1
        # max(matrix[i][i],matrix[i][2*n-1-i],matrix[2*n-1-i][i], matrix[2*n-1-i][2*n-1-i])
        print(matrix[i][j],matrix[i][2*n-1-j],matrix[2*n-1-i][j], matrix[2*n-1-i][2*n-1-j])
        s += max(matrix[i][j],matrix[i][2*n-1-j],matrix[2*n-1-i][j], matrix[2*n-1-i][2*n-1-j])
# return s
print(s)
