# bfs, queue
from collections import deque

num = int(input())
link = int(input())

graph = [ [] for i in range(num+1)]
visit = [[0]*(num+1)]

queue = deque([1])

for i in range(link):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]
visit[1] = 1

while queue:
    target = queue.popleft()
    for nx in graph[target]:
        if visit[nx] == 0:
            queue.append(nx)
            visit[nx] = 1

print(sum(visit) - 1)
