# 동전
# https://d-cron.tistory.com/23

import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):

    N = int(input().rstrip())
    coins = list(map(int, input().rstrip().split()))
    M = int(input().rstrip())

    dp = [0] * (M + 1)
    dp[0] = 1 # 0을 만드는 방법은 1가지 ex) 2원으로 0을 만드려면 2원짜리 0개가 있으면 된다.

    for coin in coins:
        for i in range(1, M + 1):
            if i - coin >= 0: 
                dp[i] += dp[i - coin] # dp[i] + (i - coin)을 만드는 방법
    
    print(dp[M])