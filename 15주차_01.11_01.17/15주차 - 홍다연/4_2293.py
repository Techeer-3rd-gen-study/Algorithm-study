# 2293번 : 동전 1

import sys
input = sys.stdin.readline

n, k = map(int, input().split())  

coins = [int(input()) for _ in range(n)]  

dp = [1] + [0] * k

for coin in coins :
    for j in range(coin, k + 1):
            if j - coin >= 0:
                dp[j] += dp[j - coin]

print(dp[k])