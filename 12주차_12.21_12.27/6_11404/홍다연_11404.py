# 11404번 : 플로이드

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())  # 도시수 
m = int(input())  # 버스수

cost = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

# 시작 도시 도착도시가 같은 경우 0으로 초기화 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            cost[i][j] = 0

# 최소 비용 갱신 
for i in range(m):
    a, b, c = map(int,input().split())
    if cost[a][b] > c:
        cost[a][b] = c

# 플로이드 워셜 
for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            cost[i][j] = min(cost[i][j],cost[i][k] + cost[k][j])

# 최소 비용 출력 , 방문하지 않아 inf인 경우 0으로 출력해준다 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == INF :
            print(0, end=' ')
        else:
            print(cost[i][j],end=' ')
    print()
