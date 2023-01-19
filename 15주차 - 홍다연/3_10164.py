# 10164번 : 격자상의 경로 

import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())  # 행, 열, O좌표 

def square(n, m) :
    dp = [[0] * (m + 1)] * (n + 1)

    for i in range(1, n + 1) :
        for j in range(1, m + 1) :
            if i == 1 and j == 1 :
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[n][m]


if k == 0 :
    print(square(n, m))
    
else :
    dotn1 = (k - 1) // m + 1
    dotm1 = k - (dotn1 - 1) * m
    dotn2 = n - (dotn1 - 1)
    dotm2 = m - (dotm1 - 1)

    case1 = square(dotn1,dotm1)
    case2 = square(dotn2,dotm2)

    print(case1*case2)