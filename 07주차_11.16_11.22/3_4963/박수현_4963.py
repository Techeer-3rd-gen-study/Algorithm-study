# 1. deque 사용
from collections import deque

# 상하좌우, 대각선까지 확인하기 위함
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def bfs(i, j):
    graph[i][j] = 0
    queue = deque()
    queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    cnt = 0
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

# 2. deque 사용X
# #상하좌우, 대각선까지 확인하기 위함
# dx = [1, -1, 0, 0, 1, -1, 1, -1]
# dy = [0, 0, -1, 1, -1, -1, 1, 1]
# def bfs(i, j):
#     graph[i][j] = 0
#     queue = [[i, j]]
#     while queue:
#         x, y = queue[0][0], queue[0][1]
#         del queue[0]
#         for k in range(8):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append([nx, ny])
# while True:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
#     graph = []
#     cnt = 0
#     for i in range(h):
#         graph.append(list(map(int, input().split())))
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1:
#                 bfs(i, j)
#                 cnt += 1
#     print(cnt)
