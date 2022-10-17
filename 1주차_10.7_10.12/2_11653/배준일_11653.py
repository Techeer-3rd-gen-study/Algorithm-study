# 소인수분해

import sys
input = sys.stdin.readline

N = int(input().rstrip())
d = 2 # 나누는 수

while N != 1 :
    if N % d == 0: # 나머지가 0 = 나누어 떨어진다.
        print(d)
        N //= d
    else :
        d += 1 # 나누는 수 증가