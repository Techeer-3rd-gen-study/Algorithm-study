# 특정 거리의 도시 찾기
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
graph = [[] for _ in range(n + 1)] # 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n + 1) # 최단거리 테이블
answer = []

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append((b, 1)) # a번 노드에서 b번 노드로 가는 비용이 1

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 비용 0, 시작 노드
    distance[start] = 0 
    
    while q:
        dist, now = heapq.heappop(q) # 현재까지의 거리, 가중치

        if distance[now] < dist: 
            continue

        for i in graph[now]: # 현재 노드와 인접한 노드들 확인
            cost = dist + i[1]

            if cost < distance[i[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # q에 저장

dijkstra(x)

for i in range(1, n + 1):
    if distance[i] == k: # 거리가 k인 값만 answer에 저장
        answer.append(i)

if len(answer) == 0: 
    print(-1)
else:
    for i in answer: 
        print(i, end = '\n')
