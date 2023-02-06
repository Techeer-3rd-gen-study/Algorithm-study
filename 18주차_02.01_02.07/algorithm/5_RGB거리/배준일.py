# RGB 거리

import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [list(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(1, N):
    # 0 = R, 1 = G, 2 = B
    # i = 1부터 자기 자신 색을 제외한 그 전 두가지 색 중 가장 비용이 작은 것을 자기 자신의 비용에 더 하기
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2]) # G, B 중 최소값 더하기
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2]) # R, B 중 최소값 더하기
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1]) # R, G 중 최소값 더하기

print(min(dp[N - 1]))