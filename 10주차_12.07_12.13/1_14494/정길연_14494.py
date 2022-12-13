# 오른쪽, 아래, 오른쪽 대각선 아래만 갈 수 있음
# 
n, m = map(int, input().split())

dp = [ [0] * (m+1)  for _ in range(n+1) ]
dp[1][1] = 1

for x in range(1, n+1):
    for y in range(1, m+1):
        if x == 1 and y ==1 :
            continue
        else:
            dp[x][y] = dp[x-1][y] + dp[x][y-1] + dp[x-1][y-1]
        
result = dp[n][m]
STANDARD = 1000000007

if result < STANDARD:
    print(result)
else:
    print(result%STANDARD)