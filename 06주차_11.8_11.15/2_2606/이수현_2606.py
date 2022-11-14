# 2606 : 바이러스

com = int(input())
pair = int(input())

matrix = [[0] * (com + 1) for _ in range(com + 1)]

for _ in range(pair):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

# 방문 노드 0으로 초기화
visited = [0] * (com + 1)

def dfs(v):
    # 시작 노드 방문처리
    visited[v] = 1

    for i in range(1, com + 1):
        # 방문하지 않은 노드라면 dfs 탐색
        if (visited[i] == 0 and matrix[v][i] == 1):
            dfs(i)

dfs(1)
print(sum(visited) - 1)