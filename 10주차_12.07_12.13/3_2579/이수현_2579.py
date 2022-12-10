# 2579 : 계단 오르기

import sys
imput = sys.stdin.readline

n = int(input())
# 계단 값 저장하는 리스트 n개로 저장하면 런타임에러(인덱스에러) 발생
stair = [0] * 301
for i in range(n):
    stair[i] = int(input())

# dp 테이블 초기화
d = [0] * 301

d[0] = stair[0]
d[1] = max(stair[0] + stair[1], stair[1])
d[2] = max(stair[0] + stair[2], stair[1] + stair[2])

# 마지막 계단을 밟아야 하므로 
# i - 2 계단 밟는 경우와 i - 3 계단 밟는 경우로 나뉨
for i in range(3, n):
    d[i] = max(d[i - 2] + stair[i], d[i - 3] + stair[i - 1] + stair[i])

print(d[n - 1])