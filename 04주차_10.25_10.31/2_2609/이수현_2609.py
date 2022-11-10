# 최대공약수와 최소공배수

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

# a*b/(최대공약수) = 최소공배수 이용해서 최소공배수 구하기
for gcd in range(min(a, b), -1, -1):
    if a % gcd == 0 and b % gcd == 0:
        print(gcd, a * b // gcd, sep = "\n")
        break

# 파이썬 내장 모듈 이용
# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))
