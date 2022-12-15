# 1965번 : 상자 넣기 
# 내앞에 위치한 상자중에서 가장 많은 상자를 포함하고 있는 나보다 작은 상자 개수에 +1을 해주어 구한다. 

n = int(input())
box = list(map(int, input().split()))

dp = [0] * 1001

for b in box:
    dp[b] = max(dp[:b]) + 1

print(max(dp))
