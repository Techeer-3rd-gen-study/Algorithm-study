# 음료수 얼려먹기 

n, m = map(int, input().split())

# 2 차원 리스트의 맵 정보 입력 받기 
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# DFS
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

    if graph[x][y] == 0 :
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True :
            result += 1

print(result)