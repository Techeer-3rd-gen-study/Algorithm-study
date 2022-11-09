import sys

input = sys.stdin.readline

row, col = map(int, input().split(" "))

# print(row," ", col)

result_matrix = [[-1 for i in range(col)] for j in range(row)]

cloud_matrix = []
for i in range(0, row):
    cloud_matrix.append(input())

for i in range(row):
    for j in range(col):
        if cloud_matrix[i][j] == "c":
            result_matrix[i][j] = 0
        elif j>0:
            if result_matrix[i][j-1] == 0:
                result_matrix[i][j] = 1
            elif result_matrix[i][j-1] > 0:
                result_matrix[i][j] = 1 + result_matrix[i][j-1]

for i in range(row):
    for j in range(col):
        print(result_matrix[i][j], end=" ")
    print()
