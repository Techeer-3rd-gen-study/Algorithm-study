# 1058 : 친구찾기

import sys
input = sys.stdin.readline
n = int(input())
graph = [list(input().strip()) for _ in range(n)]
# 2-친구 사이일 때 1, 아니면 0
friend = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 2-친구인 경우
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
                friend[i][j] = 1

result = 0
for row in friend:
    result = max(result, sum(row))
print(result)