from collections import deque

island = list()

def bfs(a, b, graph):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    q = deque()
    q.append((b,a))

    while q : 
        y, x = q.popleft()

        for i in range(8):      
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < w and 0<= ny < h):
                if graph[ny][nx] == 1:
                    q.append((ny,nx))
                    graph[ny][nx] = 0
                   
    return


while True:
    w, h = list(map(int, input().split()))
    graph = list()
    island_cnt = 0 

    if w == h == 0:
        break
    else:
        for _ in range(h):
            graph.append(list(map(int, input().split())))
        
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(i, j, graph)
                    island_cnt += 1

    island.append(island_cnt)

for i in island:
    print(i)