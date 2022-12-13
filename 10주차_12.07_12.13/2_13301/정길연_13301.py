# 둘레 길이 : 4, 6, 10, 16, 26, 42 ..
n = int(input())

dp = [0] * 81
dp[0] = 4
dp[1] = 6

if n == 1:
    print(4)
elif n == 2:
    print(6)
else: 
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n-1])