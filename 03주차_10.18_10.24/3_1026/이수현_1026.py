# 보물

import sys

N = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

s = 0

for i in range(N):
    # a 리스트 원소의 최솟값과 b 리스트 원소의 최댓값을 곱하기
    s = s + min(a) * max(b)

    # a 리스트 원소의 최솟값과 b 리스트 원소의 최댓값을 각각의 리스트에서 제거해서 반환
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(s)