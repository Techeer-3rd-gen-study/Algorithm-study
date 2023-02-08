# 2xn 타일링

import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = [0] * 1001

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] # 규칙

print(dp[n] % 10007)