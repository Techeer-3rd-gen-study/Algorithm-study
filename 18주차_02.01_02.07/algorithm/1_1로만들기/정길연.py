# 앞에서부터 일일히 해봐야함

n = int(input())

dp = [0] * (n + 1)

for i in range(2, n+1 ):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)        # 3 * 2 + 1일경우 생각해보기
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)    

print(dp[n])