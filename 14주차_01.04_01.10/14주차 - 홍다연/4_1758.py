# 1758번 : 알바생 강호 

import sys
input = sys.stdin.readline

n = int(input())
tip = [int(input()) for _ in range(n)]

tip.sort(reverse=True)
sum = 0

for i in range(n):
    if tip[i] - i < 0:
        continue

    sum += (tip[i] - i)
    
print(sum)
