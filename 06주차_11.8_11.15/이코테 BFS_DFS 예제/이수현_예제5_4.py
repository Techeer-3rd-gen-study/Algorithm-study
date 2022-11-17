# 미로탈출

from collections import deque

n, m = map(int, input().split())

# 2차원 리스트 맵 입력받기
graph = [list(map(int, input())) for _ in range(n)]

# 이동할 상하좌우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 비어있을 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dx[i]
            # 공간 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우(괴물존재) 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))
