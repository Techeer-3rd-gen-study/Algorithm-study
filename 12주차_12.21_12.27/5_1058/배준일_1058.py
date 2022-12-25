# 친구

import sys
input = sys.stdin.readline

n = int(input().rstrip())

graph = [list(input().rstrip()) for _ in range(n)]

is_friend = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: # A != A 친구 아님
                continue
            # 두 사람이 친구 또는 A = B, B = C 
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
                is_friend[i][j] = 1

res = 0

# 서로 친구인 경우 = 친구i에서 친구j까지 거리가 1
# 한 다리 건너서 아는 친구인 경우 = 친구i에서 친구j까지 거리가 2
for row in is_friend:
    res = max(res, sum(row))
print(res)