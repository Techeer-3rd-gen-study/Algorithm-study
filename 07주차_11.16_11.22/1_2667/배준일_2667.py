# 단지 번호 

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input().rstrip())
danji = []

def bfs(graph, a, b): # a, b는 좌표
    queue = deque()
    queue.append((a,b)) # queue에 추가
    graph[a][b] = 0 # 추가한 좌표 0으로 초기화
    house = 1 # (a, b) count -> 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=N or ny < 0 or ny >= N: # 좌표 밖 예외처리
                continue

            if graph[nx][ny] == 1: 
                graph[nx][ny] = 0
                queue.append((nx, ny))
                house += 1
    return house

graph = [list(map(int, input().rstrip())) for _ in range(N)] # 지도   

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            danji.append(bfs(graph, i, j))

danji.sort() # 오름차순 정렬

print(len(danji)) # 총 단지 수

for i in danji:
    print(i) # 단지 내 집의 수
