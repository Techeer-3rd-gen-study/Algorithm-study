# 1260 : DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    # 간선 입력받아서 1로 초기화
    matrix[a][b] = matrix[b][a] = 1

# 방문 노드 0으로 초기화
visited = [0] * (n + 1)

def dfs(v):
    # 시작 노드 방문처리
    visited[v] = 1
    print(v, end = ' ')

    for i in range(1, n + 1):
        # 방문하지 않은 노드라면 dfs 탐색
        if (visited[i] == 0 and matrix[v][i] == 1):
            dfs(i)

def bfs(v):
    queue = deque([v])
    # 시작 노드 방문처리(dfs를 먼저 수행하므로 1 -> 0)
    visited[v] = 0

    # 큐가 비어있을 때까지 수행
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in range(1, n + 1):
            # 방문하지 않은 노드 큐에 넣고 방문처리
            if (visited[i] == 1 and matrix[v][i] == 1):
                queue.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)