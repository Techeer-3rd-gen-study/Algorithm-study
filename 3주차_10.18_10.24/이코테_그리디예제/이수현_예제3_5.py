# 1이 될 때까지

import sys

n, k = map(int, sys.stdin.readline().split())
result = 0

while n >= k:
    while n % k != 0:
        n = n - 1
        result = result + 1
    n = n // k 
    result = result + 1

while n > 1:
    n = n - 1
    result = result + 1
print(result) 