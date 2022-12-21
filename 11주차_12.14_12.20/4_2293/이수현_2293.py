# 2293 : 동전 1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp 테이블 초기화
dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(k + 1):
        # 만들려고 하는 돈이 가지고 있는 화페단위보다 크거나 같을 경우
        if i >= coin:
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수 더하기
            dp[i] += dp[i - coin]

print(dp[k])