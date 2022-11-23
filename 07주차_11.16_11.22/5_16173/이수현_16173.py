# 16173 : 점프왕 쩰리

def dfs(x, y):
    # 구역의 외부이거나 이미 방문한 곳이라면 중지
    if x <= -1 or x >= n or y <= -1 or y >= n or visited[x][y] == 1:
        return
    
    # 오른쪽 가장 아래칸에 도달하면 중지
    if graph[x][y] == -1:
        visited[x][y] = 1
        return

    # 방문 처리   
    visited[x][y] = 1

    # 상하좌우를 칸에 적힌 수만큼 이동
    dfs(x - graph[x][y], y)
    dfs(x, y - graph[x][y])
    dfs(x + graph[x][y], y)
    dfs(x, y + graph[x][y])

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# 출발점은 0,0
dfs(0, 0)

# 오른쪽 가장 아래칸에 도달할 수 있다면
if visited[-1][-1] == 1:
    print("HaruHaru")
else:
    print("Hing")
