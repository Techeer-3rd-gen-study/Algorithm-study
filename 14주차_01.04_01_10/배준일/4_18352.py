# 특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
graph = [[] for _ in range(n + 1)]
distance = [0] * (n + 1) # 거리 리스트
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0 # 거리 초기 설정

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1 # 거리 갱신

                if distance[i] == k: # 거리가 k일 떄 추가
                    answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)