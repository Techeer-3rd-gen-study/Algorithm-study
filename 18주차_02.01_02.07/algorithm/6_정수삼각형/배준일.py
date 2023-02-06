# 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 삼각형의 크기
triangles = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(triangles[i])):
        if j == 0: # 윗 줄의 0번째 열을 더한다.
            triangles[i][j] += triangles[i - 1][j]

        elif j == len(triangles[i]) - 1: # 윗줄의 마지막 열을 더한다.
            triangles[i][j] += triangles[i - 1][j - 1]

        else:
            triangles[i][j] += max(triangles[i - 1][j - 1], triangles[i - 1][j])
    
print(max(triangles[n - 1]))