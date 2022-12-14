from collections import deque

n, m, start = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1) # 방문한 노드

for _ in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

# dfs는 재귀적
# 첫 노드를 받으면 visited에 기록하고 연결된거를 계속해 찾아가기
def dfs(start):
    print(start, end=" ")
    visited[start] = True  # 들어온 값 방문처리

    for i in range(1, n+1):
        # if visited[i] == 0 and (graph[start][i] == 1 or graph[i][start] == 1):
        # 어차피 line10에서 양방향 연결 해줬으니 두번 확인할 필요 없음
        if visited[i] == False and (graph[start][i] == 1 or graph[i][start] == 1):
            dfs(i)


# bfs는 queue
# 들어온거 주변을 먼저 탐색
def bfs(start):
    queue = deque()
    visited[start] = True
    queue.append(start)

    # queue가 빌때까지
    while queue : 
        now = queue.popleft()
        print(now, end=" ")

        for i in range(1, n+1):
            if graph[now][i] == 1 and visited[i] == False:
                queue.append(i)
                visited[i] = True
    
dfs(start)
print()
visited = [False] * (n+1)
bfs(start)

