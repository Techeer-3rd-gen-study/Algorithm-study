# 2056번 : 작업 

import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1)  # 작업 끝나는 시간 저장 

for i in range(1, n+1):
    work, count, *pre = map(int, input().split())
    dp[i] = work  # 선행 작업 이 없으면 그대로 작업 시간 저장
    for j in pre:
        dp[i] = max(dp[i], dp[j]+work)  # 가장 늦게 끝나는 선행작업 + 작업시간 더해 저장 

print(max(dp))


