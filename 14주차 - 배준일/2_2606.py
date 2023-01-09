# 바이러스

from collections import deque

n = int(input()) # 컴퓨터 수
m = int(input()) # 연결된 쌍의 수

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def bfs(v):
    global cnt
    q = deque([v])
    visited[v] = True

    while q:
        now = q.popleft()

        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

bfs(1)
print(cnt)




