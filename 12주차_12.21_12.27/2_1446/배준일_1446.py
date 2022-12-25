# 지름길

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().rstrip().split()) # 지름길의 개수, 고속도로의 길이

graph = [[] for _ in range(d + 1)] # 고속도로의 길이만큼 배열 생성 (범위가 작아서 가능) // d까지의 거리 하나하나를 노드로 본다.
distance = [INF] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1)) # 노드 i 에서 다음 노드 i+1까지의 거리는 1

for i in range(n): 
    x, y, z = map(int, input().rstrip().split()) # 지름길 시작위치, 지름길 도착위치, 지름길 길이

    if y > d: # 지름길 도착 위치가 고속도로의 길이보다 큰 경우
        continue

    graph[x].append((y, z)) # x번 노드에서 y로 가는 비용이 z


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


dijkstra(0)

print(distance[d])
