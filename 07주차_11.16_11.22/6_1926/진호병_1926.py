from collections import deque

def bfs(y, x):
    graph[y][x] = 0
    queue = deque()
    queue.append((y, x))
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < n) and (0 <= X < m) and graph[Y][X] == 1:
                queue.append((Y, X))
                graph[Y][X] = 0
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res.append(bfs(i, j))
print(len(res))
print(max(res) if res else 0)