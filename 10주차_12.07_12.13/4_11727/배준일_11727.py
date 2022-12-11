# 2*n 타일링 2

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

dp[0] = 1
dp[1] = 1
# n = 1 : " l " (1x2 타일 하나)

# n = 2 : " ll ", " = " (2x2 타일 하나)

# n = 3 : " lll " , " l= ", " =l ",(1x2타일 1개, 2x2타일 1개)

# n = 4 : " llll ", " l=l ", " =ll ", " ll= ", == "

# 점화식에 따른 경우의 수 계산
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[n] % 10007)