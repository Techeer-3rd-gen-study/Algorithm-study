# ATM

import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

# 인출 시간 오름차순 정렬 
time.sort()

result = 0

for i in range(1, N + 1):
    # 자기 인출 순서까지 더하기
    result = result + sum(time[ : i])

print(result)