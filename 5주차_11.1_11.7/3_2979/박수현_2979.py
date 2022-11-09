import sys

input = sys.stdin.readline

pay = list(map(int, input().split(" ")))

parking = []
for i in range(0, 3):
    parking.append(list(map(int, input().split(" "))))

matrix = [[0 for col in range(100)] for row in range(3)]

for i in range(0, 3):
    for j in range(parking[i][0], parking[i][1]):
        matrix[i][j] = 1

result = 0
for j in range(min(parking[0][0], parking[1][0], parking[2][0]), max(parking[0][1], parking[1][1], parking[2][1])):
    if matrix[0][j] == 1 and matrix[1][j] == 1 and matrix[2][j] == 1:
        result += pay[2]*3
    elif (matrix[0][j] == 1 and matrix[1][j] == 1) or (matrix[1][j] == 1 and matrix[2][j] == 1) or (matrix[0][j] == 1 and matrix[2][j] == 1):
        result += pay[1]*2
    elif matrix[0][j] == 1 or matrix[1][j] == 1 or matrix[2][j] == 1:
        result += pay[0]*1

print(result)
