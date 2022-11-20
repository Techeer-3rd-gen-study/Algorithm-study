# 백준 1926번 : 그림
# 대각선으로 연결 X, 그림의 개수 와 가장 큰 그림의 넓이 출력 
# 1은 그림, 0 은 빈공간 

from collections import deque
import sys
input = sys.stdin.readline

# BFS 코드 구현 
def bfs(graph, x, y) :
    queue = deque()
    queue.append((x,y))

    graph[x][y] = 0
    count = 1

    while queue : 
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0 
                queue.append((nx,ny))
                count += 1
    return count


n, m = map(int, input().split())   # 도화지 크기 
graph = []                         
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


size = []  # 그림 크기 저장 리스트

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 :  
            size.append(bfs(graph, i, j))    


if len(size) == 0 :  # 그림이 없을 경우 
    print(0)
    print(0)
else :
    print(len(size))
    print(max(size))