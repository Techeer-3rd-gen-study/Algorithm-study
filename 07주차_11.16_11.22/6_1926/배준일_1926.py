# 그림

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().rstrip().split())

drawing_list = []

def bfs(graph, a, b): # a, b는 좌표
    queue = deque()
    queue.append((a,b)) # queue에 추가
    graph[a][b] = 0 # 추가한 좌표 0으로 초기화
    drawing = 1 # (a, b) count -> 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= m: # 좌표 밖 예외처리
                continue

            if graph[nx][ny] == 1: # 그림일 때
                graph[nx][ny] = 0
                queue.append((nx, ny))
                drawing += 1
    return drawing

graph = [list(map(int, input().rstrip().split())) for _ in range(n)] # 도화지 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            drawing_list.append(bfs(graph, i, j))

drawing_list.sort() # 오름차순 정렬

if len(drawing_list) == 0 :  # 그림이 없을 경우 
    print(0)
    print(0)
else:
    print(len(drawing_list)) # 총 그림 수
    print(drawing_list[-1]) # 가장 넓은 그림의 넓이