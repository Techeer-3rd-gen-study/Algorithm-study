

#2156
n = int(input())

juice = [0] * 10001

for i in range(n):
  juice[i] = int(input())

dp = [0] * 10001

dp[0] = juice[0]

dp[1] = juice[0] + juice[1]

dp[2] = max(juice[1]+juice[2], juice[0]+juice[2], juice[0]+ juice[1])

for i in range(3,n):
  dp[i] = max(dp[i-3] + juice[i-1] + juice[i], dp[i-2] + juice[i],dp[i-1])
# 마시지 않는것을 고려해야함 

print(dp[i])
