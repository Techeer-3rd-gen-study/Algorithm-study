# 다이나믹이 뭐예요?

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 1 # 시작점

for x in range(1, n + 1):
    for y in range(1, m + 1):
        if x==1 and y==1: # 시작점일때 continue
            continue
        
        # dp[x - 1][y] = ->
        # dp[x][y - 1] = ↓ (아래)
        # dp[x - 1][y - 1] = ↘ (오른쪽 아래)
        dp[x][y] = dp[x - 1][y] + dp[x][y - 1] + dp[x - 1][y - 1] 

print(dp[n][m] % (int(1e9) + 7))
