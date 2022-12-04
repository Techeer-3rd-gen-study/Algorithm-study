# 1654 : 랜선 자르기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start = 1
end = max(lan)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    # 만들 수 있는 랜선 개수 총합
    for x in lan:
        total += (x // mid)

    # 랜선 만든 경우
    if total >= n:
        result = mid
        start = mid + 1
    # 랜선 못 만든 경우
    else:
        end = mid - 1

print(result)