string = '''11 2 4
4 5 6
10 8 -12'''

n = 3

arr = []

for _ in range(n):
    arr.append(list(map(int, string.rstrip().split())))

# result = diagonalDifference(arr)



arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]

n = len(arr[0])
d1, d2 = 0, 0
for i in range(n):
    d1 += arr[i][n-i-1]
    d2 += arr[i][i]
    print(i, arr[i][n-i-1], arr[n-1-i][i])
abs(d1-d2)
# return abs(arr[0][0] + arr[2][2] - arr[0][2] - arr[2][0])

