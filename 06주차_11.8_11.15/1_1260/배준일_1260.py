# DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline 

# N = 정점의 개수, M = 간선의 개수, V = 탐색을 시작할 정점의 번호(root)
N, M, V = map(int,input().split())

visited=[False]*(N+1) # 인덱스 0은 사용안함

graph=[[] for _ in range(N+1)] # 간선의 개수 + 1 만큼 생성

for _ in range(M):
    a, b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 간선이 양방향이라 둘 다 저장
    # ex) graph[1] = [2], graph=[2]=[1]

for i in range(len(graph)):
    graph[i].sort()
    # 그래프 정렬 // 정점 번호가 작은 것을 먼저 방문

def dfs(V):

    print(V, end=' ')
    visited[V] = True

    for i in graph[V]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

def bfs(V):

    q = deque([V])

    visited[V] = True

    while q:
        now=q.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(V)

visited=[False]*(N+1) # bfs를 위해 visited False로 초기화
print()

bfs(V)
