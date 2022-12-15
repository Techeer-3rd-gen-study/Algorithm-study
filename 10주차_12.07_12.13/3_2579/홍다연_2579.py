# 백준 2579번 : 계단 오르기 

# 3번째 계단 - d[3] = stair[1]+stair[3] 또는 stair[2]+stair[3] 중 큰 값
# 4번째 계단 - d[4] = stair[1]+stair[2]+stair[4] 또는 stair[1]+stair[3]+stair[4] 중 큰 값
# 5번째 계단 - d[5] = stair[1]+stair[2]+stair[4]+stair[5] 또는 stair[1]+stair[3]+stair[5] 중 큰 값
# 그러므로, i 번째 계단은 
# d[i] = d[i - 3] + stair[i - 1]+ stair[i] 또는 d[i-2] + stair[i] 중 큰 값을 가진다. 

n = int(input())

stair = [0] * 301
d = [0] * 301

for i in range(1, n + 1):
    stair[i] = int(input())


d[1] = stair[1]
d[2] = stair[1] + stair[2]
d[3] = max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, n + 1):
    d[i] = max(d[i-3] + stair[i-1] + stair[i], d[i-2] + stair[i])

print(d[n])

