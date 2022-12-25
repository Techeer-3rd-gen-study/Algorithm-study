# 1916 : 최소비용 구하기
# 모르겠어서 답을 가져왔습니다...
# https://resilient-923.tistory.com/338

import sys,heapq
input = sys.stdin.readline

INF = 987654321
n = int(input())
m = int(input())
data = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    # b가 노드 c 가 경로
    a,b,c = map(int,input().split())
    data[a].append((b,c))
start,end = map(int,input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0
    while q:
        now_node, dist = heapq.heappop(q)
        if distance[now_node] < dist:
            continue
        for n_n, weight in data[now_node]:
            cost = dist + weight
            if cost < distance[n_n]:
                distance[n_n] = cost
                heapq.heappush(q,(n_n,cost))

dijkstra(start)
print(distance[end])