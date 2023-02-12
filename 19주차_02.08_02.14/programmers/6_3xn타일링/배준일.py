# 3 x n 타일링

def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11

    for i in range(4, n + 1, 2): # 시작 : 4, 끝 : n + 1, 2씩 증가
        dp[i] = dp[i - 2] * 3 # 1번
        
        for j in range(i - 4, -1, -2): # 시작 : i - 4, 끝 : -1, -2씩 감소
            dp[i] += dp[j] * 2 # 2번
        
        dp[i] = (dp[i] + 2) % 1000000007 # 3번, 나머지 계산
    
    return dp[n]