# 섬의 개수

import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1] # 상하좌우 대각선까지 체크
dy = [0, 0, -1, 1, -1, 1, 1, -1] 

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b)) # 튜플()이든 리스트[]든 상관없다.
    graph[a][b] = 0 # 추가한 좌표 0으로 초기화

    while queue:
        x, y = queue.popleft()

        for i in range(8): # 상하좌우 대각선 = 8
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1: # 좌표밖이 아니고 섬일 때
                graph[nx][ny] = 0 # 0으로 왔던 곳 체크
                queue.append((nx, ny)) # 큐에 추가

while True:
    w, h = map(int, input().rstrip().split()) # 넓이, 높이
    graph = []
    island = 0
    # 0, 0이면 break
    if w == 0 and h == 0:
        break

    for _ in range(h):
        graph.append(list(map(int, input().rstrip().split())))
    
    for a in range(h):
        for b in range(w):
            if graph[a][b] == 1: # 섬일때 탐색시작
                bfs(graph, a, b)
                island += 1 # 섬 ++
    print(island)
    