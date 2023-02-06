#2 계단 오르기 
# https://www.acmicpc.net/problem/2579

n = int(input()) 
s = [int(input()) for _ in range(n)]

dp = [0]*(n) 

if len(s) <= 2 : 
    print(sum(s))

else: 
    dp[0] = s[0] 
    dp[1] = s[0] + s[1] 
    for i in range(2,n) : 
        
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])

    print(dp[-1])

