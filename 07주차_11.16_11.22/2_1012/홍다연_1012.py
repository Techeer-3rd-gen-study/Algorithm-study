# 백준 1012번 유기농 배추 
from collections import deque


# bfs 메소드 이용 
def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 떄까지
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return


# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = int(input())   # 테스트 케이스 수 

for i in range (t):
    count = 0
    n, m, k = map(int,input().split())
    graph = [ [0] * m for _ in range(n) ] 

    # 배추 좌표값 입력 
    for j in range(k) :   
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                count += 1

    print(count)
 


