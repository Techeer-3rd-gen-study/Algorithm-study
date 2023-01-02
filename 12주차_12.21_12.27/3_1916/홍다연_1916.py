# 1916번 : 최소 비용 구하기
# https://chaemi720.tistory.com/177?category=997677

import heapq, sys
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    # 출발 도시, 도착 도시, 비용
    s, e, cost = map(int,input().split())
    graph[s].append([cost,e])

start, end = map(int, input().split())  # 출발도시, 도착도시 

INF = int(1e9)
distance = [INF] * (N + 1)

distance[start] = 0  # 시작점 = 비용 0

heap = [[0,start]]  # [비용,다음 도시]

while heap:
    cost, e = heapq.heappop(heap)
    # e(버스 도착도시)로 가는 비용이 최소비용으로 갱신된 후 값이면 버리기
    if distance[e] != cost:
        continue

    for a, b in graph[e]:
        if distance[b] > cost + a:
            distance[b] = cost + a
            heapq.heappush(heap, [distance[b], b])  # 이전 이동 거리보다 e를 거치는 게 더 최소 비용이면 갱신


print(distance[end])
