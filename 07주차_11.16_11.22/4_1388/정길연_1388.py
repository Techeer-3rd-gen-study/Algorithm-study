# -은 좌우만 확인
# |은 상하만 확인
# bfs
from collections import deque

n, m = list(map(int, input().split())) # n: 세로,  m: 가로
graph = []
for _ in range(n):
    graph.append(list(input()))

tile_cnt = 0
q = deque()

def bfs(a, b, graph, target):
    global tile_cnt
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q.append((b,a))

    while q :
        y, x = q.popleft()

        if target == '-':
            for i in range(0,2):
                nx = x + dx[i]
                ny = y + dy[i]
                if( 0<= nx < m and 0<= ny < n and graph[ny][nx] == target ):
                    graph[ny][nx] = 0
                    q.append((ny, nx))
                   
        elif target == '|':
            for i in range(2,4): 
                nx = x + dx[i]
                ny = y + dy[i]
                if( 0<= nx < m and 0<= ny < n and graph[ny][nx] == target ):
                    graph[ny][nx] = 0
                    q.append((ny, nx))
                    


for i in range(n):
    for j in range(m):
        if graph[i][j] == '-':
            bfs (j, i, graph, '-')
            tile_cnt += 1
        elif graph[i][j] == '|':
            bfs (j, i, graph, '|')
            tile_cnt += 1
        else:
            pass

print(tile_cnt)