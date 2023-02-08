# 1, 2, 3 더하기

import sys
input = sys.stdin.readline

dp=[0] * 11
dp[1] = 1 # 1+1
dp[2] = 2 # 1+1, 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3
dp[4] = 7 # 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1

for i in range(4, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    print(dp[n])
