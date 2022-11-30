# 2230 : 수 고르기

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

list = [int(input()) for _ in range(n)]
list.sort()

start, end = 0, 0
min_value = int(2e9)

while start < n and end < n:
    result = list[end] - list[start]
    
    # 차이가 m보다 크다면
    if result >= m:
        min_value = min(list[end] - list[start], min_value)
        start += 1
    # 차이가 m보다 작다면
    else:
        end += 1

print(min_value)