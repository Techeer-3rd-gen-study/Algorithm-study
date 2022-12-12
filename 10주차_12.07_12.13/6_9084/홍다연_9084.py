# 9084번 : 동전 
# https://d-cron.tistory.com/23 

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    coins = list(map(int, input()).split())
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, m + 1):
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[m])