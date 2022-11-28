# 백준 4963번 : 섬의 개수 

from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    global w, h, count, graph

    graph[x][y] = 0
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        dx = [1, -1, 0, 0, 1, -1, 1, -1]   # 대각선 추가
        dy = [0, 0, -1, 1, -1, 1, 1, -1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:  # 섬의 범위 
                graph[nx][ny] = 0
                queue.append([nx, ny])


def logic() : 
    global w, h, graph, count

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:    # 종료문 조건
            break

        graph = []
        count = 0

        for _ in range(h):    
            graph.append(list(map(int, input().split())))

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(i, j)
                    count += 1
        print(count)

logic()