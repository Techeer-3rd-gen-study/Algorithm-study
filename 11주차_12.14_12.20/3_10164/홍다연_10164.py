# 10164번 : 격자상의 경로 
# 32점...

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())  # 행,열,O좌표

dp = [[0] * (m + 1) for i in range(n + 1)]
dp[0][1] = 1  # 초기값 1로 설정 


if k != 0 :   # k의 좌표 값 
    a = k // m + 1
    b = k % m


for i in range (1, n+1) :
    for j in range (1, m+1) :
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if k == 0 :
    print(dp[n][m])
else :
    answer = dp[a][b] * dp[n - a + 1][m - b + 1]
    print(answer)

