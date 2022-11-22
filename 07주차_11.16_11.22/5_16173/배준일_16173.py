# 점프왕 쩰리

from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0] # 오른쪽
dy = [0, 1] # 아래

N = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)] # map
visited = [[False]*3 for _ in range(N)]

def bfs(graph, a, b): # a, b는 좌표
    queue = deque()
    queue.append((a,b)) # queue에 추가    

    while queue:
        x, y = queue.popleft()

        if graph[x][y] == -1: # 오른쪽 아래 도달
            return True
        
        jump = graph[x][y]
        
        for i in range(2): # 오른쪽, 아래 탐색
            # 이동방향 * 밟고있는 숫자
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump

            if nx < 0 or nx >=N or ny < 0 or ny >= N: # 좌표 밖 예외처리
                continue

            if not visited[nx][ny]: # 방문하지 않았을 때
                visited[nx][ny] = True
                queue.append((nx, ny)) # queue에 추가

if bfs(graph, 0, 0): # 시작점 (0, 0)
    print('HaruHaru')
else:
    print('Hing')
