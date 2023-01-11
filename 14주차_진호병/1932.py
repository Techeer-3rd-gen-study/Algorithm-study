

#1932 
n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(i+1):
    if j == 0 :
      dp[i][j] = dp[i][j] + dp[i-1][j]
    elif j == i : 
      dp[i][j] = dp[i][j] + dp[i-1][j-1]
    else :
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]

print(max(dp[n-1]))
# 아래에서 위로 올라가도록 할 수 있음 


