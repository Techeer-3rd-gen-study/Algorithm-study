# 12865번 : 평범한 배낭
# https://hongcoding.tistory.com/50 https://claude-u.tistory.com/208 -> 냅색 알고리즘 
# 점화식 : max(현재 물건 가치 + dp[이전 물건][현재 가방 무게 - 현재 물건 무게], dp[이전 물건][현재 가방 무게])

import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 물건 개수, 최대 무게 

thing = [[0,0]]                   # 물건 무게, 물건 가치 
for _ in range(n):
    thing.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0] # 무게 
        v = thing[i][1] # 가치 

        if j < w:  # 해당 배낭의 최대 무게보다 넣을 무게가 크다면 넣지않고, 그대로 가져온다. 
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
