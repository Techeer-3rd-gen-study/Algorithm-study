# 상자넣기

import sys
input = sys.stdin.readline

n = int(input().rstrip())
box = list(map(int, input().rstrip().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]: # 상자 값이 크면
            dp[i] = max(dp[i], dp[j] + 1) # dp[j] + 1 -> dp[j]가 담고있는 상자의 개수 + 1(자기 자신)

print(max(dp))

