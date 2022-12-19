# 2133번 : 타일 채우기 
# https://hongcoding.tistory.com/84
# 가로의 길이가 홀수 일수는 없다. 
# 가로의 길이가 2일때 -> 3가지 경우 | 가로의 길이가 4일 때 -> 11개의 경우 

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 31
dp[2] = 3

if n % 2 != 0 :
    print(0)

else :
    for i in range (4, n+1, 2):
        dp[i] = 3 * dp[i - 2] + 2

        for j in range (4, i, 2):
            dp[i] += 2 * dp[i - j]

    print(dp[n])    
