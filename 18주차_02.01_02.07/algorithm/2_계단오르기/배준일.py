# 계단 오르기

import sys
input = sys.stdin.readline

n = int(input().rstrip())
stair = [0] * 301
for i in range(n):
    stair[i] = int(input().rstrip())

dp = [0] * 301

dp[0] = stair[0] # 첫번째 계단
dp[1] = stair[0] + stair[1] # 두번째 계단
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2]) # 3번째 계단

for i in range(3, n):
    # 한 칸전 계단을 밟고 올라온 경우, 두칸 전 계단을 밟고 올라온 경우
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i],
    dp[i - 2] + stair[i])

print(dp[n - 1])
