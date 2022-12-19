# 2293번 : 동전1
# x원짜리 동전을 추가할 때 dp[k] += dp[k-x] 점화식 성립

import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 동전 종류수, 목표 금액
coin = [int(input()) for _ in range(n)]   # 동전 금액

dp = [1] + [0] * k

for i in coin :
    for j in range(i, k + 1):
            dp[j] += dp[j - i]

print(dp[k])
