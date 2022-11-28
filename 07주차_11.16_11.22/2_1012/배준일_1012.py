# 유기농 배추

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

def bfs(graph, a, b): # a, b는 좌표
    queue = deque()
    queue.append((a,b)) # queue에 추가
    graph[a][b] = 0 # 추가한 좌표 0으로 초기화

    while queue:
        x, y = queue.popleft()
        
        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=N or ny < 0 or ny >= M: # 좌표 밖 예외처리
                continue

            if graph[nx][ny] == 1: # 배추가 있을 때
                graph[nx][ny] = 0 # 0으로 초기화
                queue.append((nx, ny)) # queue에 추가


for i in range(T):
    white_earthworm = 0
    N, M, K = map(int,input().split())
    graph = [[0] * M for _ in range(N)] # 배추밭

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1 # 배추 위치 표시

    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1: # 배추일 때 bfs
                bfs(graph, a, b)
                white_earthworm += 1 # 지렁이 ++
    print(white_earthworm)