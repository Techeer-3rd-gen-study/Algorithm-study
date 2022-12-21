# 11048 : 이동하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip().split())) for _ in range(n)]
# dp 테이블 설정
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # d[i - 1][j] : ↓
        # d[i][j - 1] : →
        # d[i - 1][j - 1] : ↘
        # 3방향 중 사탕 최댓값과 이전 위치 사탕값 더하기
        dp[i][j] = maze[i - 1][j - 1] + max(dp[i - 1][j] , dp[i][j - 1],  dp[i - 1][j - 1])

print(dp[n][m])