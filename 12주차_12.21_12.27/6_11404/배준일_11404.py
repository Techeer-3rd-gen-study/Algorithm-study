# 플로이드

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip()) # 도시의 개수
m = int(input().rstrip()) # 버스의 개수

graph = [[INF] * (n + 1) for _ in range(n + 1)] 

for i in range(1, n + 1): # 자기자신으로 가는 비용 0으로 초기화
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split()) # 시작도시, 도착 도시, 비용
    graph[a][b] = min(c, graph[a][b])   # 노선이 하나가 아닐 수 있음 > 최소값 넣기 

# 플로이드 워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("0",  end=" ")
        else:
            print(graph[a][b], end=" ")
    print()