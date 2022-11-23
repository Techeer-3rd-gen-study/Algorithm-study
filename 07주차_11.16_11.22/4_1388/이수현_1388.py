# 1388 : 바닥 장식

def dfs(x, y):
    # 벽을 만나면 False 반환
    if x < -1 or x > n - 1 or y < -1 or y > m - 1:
        return False
    
    # 이미 방문했던 곳이라면 False 반환
    if visited[x][y] == True:
        return False
    
    # 현재 위치 방문 처리
    visited[x][y] = True

    # '-'이고 다음 모양도 '-'라면
    if floor[x][y] == '-' and (y == m - 1 or floor[x][y + 1] == '-'):
        dfs(x, y + 1) 

    # '|'이고 다음 모양도 '|'라면
    elif floor[x][y] == '|' and (x == n - 1 or floor[x + 1][y] == '|'):
        dfs(x + 1, y) # 아래쪽으로 이동
    return True

n, m = map(int, input().split())
floor = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
    
count = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y) == True:
            count += 1
            
print(count)