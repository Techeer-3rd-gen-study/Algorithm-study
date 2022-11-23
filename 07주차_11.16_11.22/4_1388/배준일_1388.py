# 바닥 장식

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().rstrip().split())
floor_lst = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

wood = 0


def bfs(graph, a, b, ch):
    queue = deque()
    queue.append((a, b)) # append로 안하면 a, b 따로 들어가니 조심하자
    graph[a][b] = '#' # 추가한 좌표 #으로 초기화

    while queue:
        x, y = queue.popleft()

        for i in range(2): 

            if ch == '-': # - 일 때 ny 값 이용해서 가로값 체크
                nx = x
                ny = y + dy[i+2]

            elif ch == '|': # ㅣ 일 때 nx 값 이용해서 세로값 체크
                nx = x + dx[i]
                ny = y

            elif ch == '#': # #으로 초기화했을 때
                continue

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == ch: 
                graph[nx][ny] = '#' # #으로 왔던 곳 체크
                queue.append((nx, ny)) # 큐에 추가

for i in range(N):
    for j in range(M):
        if floor_lst[i][j] == '-':
            bfs(floor_lst, i, j, '-')
            wood += 1
            
        elif floor_lst[i][j] == '|':
            bfs(floor_lst, i, j, '|')
            wood += 1
        elif floor_lst[i][j] == '#':
            continue

print(wood)