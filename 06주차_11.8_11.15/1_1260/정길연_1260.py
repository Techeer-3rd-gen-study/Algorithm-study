# dfs : 인접행렬 + 재귀, bfs : 큐
# 정점번호가 0이아닌, 1부터 시작한다는 점 주의

from collections import deque

n, m, start = map(int, input().split())

graph = [[0] * (n+1) for i in range(n+1)]
for i in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visit = [0 for _ in range(n+1)]


def dfs(start):
    print(start, end=' ')
    visit[start] = 1

    for i in range(1, n+1):
        if visit[i] == 0 and graph[x][y] == 1:
            dfs(i)

def bfs(start):
    queue = deque()
    queue = [start]
    visit[start] = 0
    
    while(queue) :
        start = queue[0]
        print(start, end=' ')

        del queue[0]  # pop이랑 헷갈리지말기

        for i in range(1, n+1):
            if visit[i] == 1 and graph[start][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(start)
print()
bfs(start)

        


