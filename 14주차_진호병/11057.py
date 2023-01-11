
# 11057
# n = int(input())

# dp =[0] * 1001
# dp[1] = 10 
# dp[2] = 55
# dp[3] = 220

# if n > 3:
#   for i in range(4,n+1): # 1부터 시작 
#     sum = 0
#     for j in range(10):
#       sum += (dp[i-2]-j)*(dp[i-2]-j + 1) / 2 
#     dp[i] = sum 

#   print(int(dp[n]))
# else : 
#   print(dp[n])

# 11057 답
n = int(input())
dp = [1]*10
for i in range(1,n) :
    for j in range(1,10) :
        dp[j] += dp[j-1]

print(sum(dp)%10007)