# 1446 : 지름길

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(d + 1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (d + 1)

# 거리 1로 초기화
for i in range(d):
    graph[i].append((i + 1, 1))

#지름길 있는 경우에 업데이트
for _ in range(n):
    a, b, c = map(int,input().split())
    if b > d:
        continue
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distance[d])