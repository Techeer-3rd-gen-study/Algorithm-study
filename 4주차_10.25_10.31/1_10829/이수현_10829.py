# 이진수 변환

import sys

def binary(r, n):
    if n == 0:
        return r
    elif n % 2 == 1:
        return binary("1" + r, n // 2)
    else:
        return binary("0" + r, n //2)

print(binary(" ", int(sys.stdin.readline())))