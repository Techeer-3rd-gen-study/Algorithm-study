n,m,k = map(int, input().split())


def solution(n,m) :
  dp = [[0] * (m+1)] * (n+1)
  for i in range(1,n+1):
    for j in range(1,m+1):
      if i == 1 and j == 1: 
        dp[i][j] = 1 
        continue
      dp[i][j] = dp[i-1][j] + dp[i][j-1]
  return dp[n][m]

if k == 0 : 
  print(solution(n,m))
else :
  x1 = (k-1)//m + 1
  y1 = k - (x1-1)*m
  x2 = n - (x1-1)
  y2 = m - (y1-1)

  beforeVia = solution(x1,y1)
  afterVia = solution(x2,y2)

  print(beforeVia * afterVia)
