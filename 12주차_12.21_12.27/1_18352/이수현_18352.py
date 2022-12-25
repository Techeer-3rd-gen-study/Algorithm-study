# 18352 : 특정 거리의 도시 찾기

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블 무한으로 초기화
dist = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # a노드에서 b번 노드로 가는 비용이 1로 초기화
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        d, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist[now] < d:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = d + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(x)
result = []
for i in range(1, n + 1):
    if dist[i] == k:
        result.append(i)

# 최단 거리가 k인 도시가 하나도 존재하지 않는 경우
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i, sep = ' ')
        