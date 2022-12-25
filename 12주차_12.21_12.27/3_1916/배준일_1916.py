# 최소비용 구하기

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip()) # 도시의 개수
m = int(input().rstrip()) # 버스의 개수

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c)) # a번 노드에서 b번 노드로 가는 비용이 c

start, end = map(int, input().rstrip().split()) # 시작번호, 도착번호

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 비용 0, 시작 노드
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 현재까지의 거리, 가중치
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # q에 저장

dijkstra(start)

print(distance[end])