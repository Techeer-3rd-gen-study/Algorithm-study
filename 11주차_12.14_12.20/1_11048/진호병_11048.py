n,m = map(int, input().split())

miro = []
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for _ in range(n):
  miro.append(list(map(int,input().split())))

for i in range(1,n+1):
  for j in range(1,m+1) : 
    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + miro[i-1][j-1]

print(dp[n][m])


