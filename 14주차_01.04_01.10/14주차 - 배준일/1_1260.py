# DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline 

N, M, V = map(int, input().rstrip().split())

visited = [False] * (N + 1)
graph=[[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(v):

    print(v, end = " ")
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

def bfs(v):
    q = deque([v])

    visited[v] = True

    while q:
        now = q.popleft()
        print(now, end = " ")

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(V)

visited = [False] * (N + 1)
print()

bfs(V)