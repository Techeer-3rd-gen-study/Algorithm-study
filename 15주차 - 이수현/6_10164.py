# 10164 : 격자상의 경로

import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

# dp 테이블
dp = [[0] * (m + 1) for _ in range(n + 1)]
# 초기화
dp[0][1], count = 1, 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # k일 시 현재 위치 저장
        if count == k:
            sx = i
            sy = j
        # k 찾기 위해 1씩 증가
        count += 1
        # 아래로 가는 경우와 오른쪽으로 가는 경우 더하기
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if k == 0:
    print(dp[n][m])

# k위치까지 가는 경우의 수와 k부터 끝점까지 가는 경우의 수 곱하기
else:
    print(dp[sx][sy] * dp[n - sx + 1][m - sy + 1])
