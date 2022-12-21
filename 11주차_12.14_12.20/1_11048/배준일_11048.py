# 이동하기

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) 
candy = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]
# dp = [[0] * (m + 1)] * (n + 1) 으로 값을 선언하면 dp[i][1]이 변경될 때 dp[0][1], dp[1][1], dp[2][1], dp[3][1]이 다 변경된다. 주의하자.

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] =  max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + candy[i - 1][j - 1] # dp값 + 현재 위치의 사탕

print(dp[n][m])
