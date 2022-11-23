# 4963 : 섬의 개수

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 상하좌우대각선
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    # 탐색한 땅 0으로 바꾸기
    graph[x][y] = 0

    for i in range(8):
        # 상하좌우대각선 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        # 아직 탐색하지 않은 땅이 있다면 dfs 탐색
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    # 지도의 영역이 0이라면 중지
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    count = 0
    # 땅(1)일 때만 dfs 탐색  
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1
  
    print(count)