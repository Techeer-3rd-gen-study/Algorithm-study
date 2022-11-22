from collections import deque

n, m = list(map(int, input().split())) # 세로:n, 가로:m

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()

graph = []
area_list = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(a,b, graph):
    area = 0
    q.append((b, a))

    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if( 0<= nx < m and 0<= ny < n and graph[ny][nx] == 1) :
                graph[ny][nx] = 0
                q.append((ny, nx))
                area += 1
    return area

drawing_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            area_list.append(bfs(i, j, graph))
            drawing_cnt += 1

if drawing_cnt == 0 :
    result = 0
else : 
    result = max(area_list)
    
print(drawing_cnt)
print(result)