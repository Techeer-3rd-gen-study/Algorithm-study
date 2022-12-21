# 동전 1
# https://mong9data.tistory.com/68

import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split()) # 동전, k원
coins = [int(input().rstrip()) for _ in range(n)] # 동전의 종류
dp = [0] * (k + 1)
dp[0] = 1 

for coin in coins:
    for j in range(coin, k + 1):
        if j - coin >= 0:
            dp[j] += dp[j - coin]

print(dp[k])