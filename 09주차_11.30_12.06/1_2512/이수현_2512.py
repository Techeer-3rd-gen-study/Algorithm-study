# 2512 : 예산

import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int, input().rstrip().split()))
m = int(input())

start = 0
end = max(request)

result = 0  # 상한액
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in request:
        # 요청한 예산이 상한액보다 크거나 같을 경우
        if x >= mid:
            total += mid
        # 요청한 예산이 상한액보다 작을 경우
        else:
            total += x
    # 예산이 충분할 경우
    if total <= m:
            result = mid
            start = mid + 1
    # 예산 넘을 경우
    else:
        end = mid - 1

print(result)