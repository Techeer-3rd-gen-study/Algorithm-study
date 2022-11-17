from collections import deque

n, m = map(int, input().split())

gragh = []
for i in range(n):
    gragh.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > 0 or ny > 0 or nx >= n or ny <= m:
                continue
            if gragh[i][j] == -1:
                gragh[nx][ny] = gragh[i][y] + 1
                queue.append((nx, ny))
                
    return gragh[n-1][m-1]

print(bfs(0,0))
            


