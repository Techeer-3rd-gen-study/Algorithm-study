# 1012 : 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(x, y):
    # 땅을 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if matrix[x][y] == 1:
        # 해당 노드 방문처리
        matrix[x][y] = 0
        # 상하좌우 위치 모두 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * (m + 1) for _ in range(n + 1)]

    # 그래프 생성
    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    count = 0
    for i in range(n):
            for j in range(m):
                # 배추가 있다면
                if dfs(i, j) == True:
                    dfs(i, j)
                    count += 1
    print(count)