# 도움을 받은 링크 주소입니다
# https://pacific-ocean.tistory.com/439

n, m, k = map(int, input().split())
dp = [[0] * (m + 1) for i in range(n + 1)]
dp[0][1], cnt = 1, 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if cnt == k:
            px = i
            py = j
        cnt += 1
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if k == 0:
    print(dp[n][m])
else:
    print(dp[px][py] * dp[n - px + 1][m - py + 1])
