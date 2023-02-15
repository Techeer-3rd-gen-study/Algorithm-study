def solution(n):
    answer = 0
    if n % 2 != 0 and n == 1:
        return answer
    dp = [0] * (n+1)
    dp[2] = 3
    dp[4] = dp[2]*3 + 2
    
    if n == 2:
        return dp[2]
    elif n == 4:
        return dp[4]
    
    for i in range(6, n+1, 2):
        dp[i] = dp[i-2] * 3 + dp[i-2] - dp[i-4]
    
    answer = dp[n] % 1000000007
        
    return answer