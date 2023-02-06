# 1463 : 1로 만들기

n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    # 2, 3으로 나누어 떨어지지 않는 수는 1을 뺴야 함
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])