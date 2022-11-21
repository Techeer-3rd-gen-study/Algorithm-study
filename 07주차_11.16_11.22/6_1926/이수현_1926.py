# 1926 : 그림
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(x, y):
    global count
    # 도화지를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 1:
        # 그림 넓이
        count += 1
        # 해당 노드 방문처리
        graph[x][y] = 0
        # 상하좌우 위치 모두 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

result = 0
count = 0
area = []

for i in range(n):
    for j in range(m):
        # 그림이 있다면
        if dfs(i, j) == True:
            # 각 그림당 그림 넓이 추가
            area.append(count)
            # 그림의 수 추가
            result += 1
            # 초기화
            count = 0

if len(area) == 0:
    print(0, 0, sep = '\n')
else:
    print(result)
    print(max(area))