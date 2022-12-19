# (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동가능
# 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다
# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값

n, m = map(int, input().split())

dp = [ [0] * (m + 1) for i in range(n + 1) ]
candy = []

for i in range(n):
    candy.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = candy[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[n][m])