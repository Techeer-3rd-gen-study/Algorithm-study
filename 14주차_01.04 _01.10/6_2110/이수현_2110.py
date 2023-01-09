# 2110 : 공유기 설치

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input().rstrip()) for _ in range(n)]

houses.sort()

start, end = 1, (houses[-1] - houses[0])

result = 0
while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    for i in range(1, len(houses)):
        # 집 사이의 거리가 mid 보다 크면 공유기 설치
        if houses[i] - current >= mid:
            current = houses[i]
            count += 1
    # 공유기 부족하면 mid 증가
    if count >= c:
        result = mid
        start = mid + 1
    # 공유기 남으면 mid 감소
    else:
        end = mid - 1

print(result)
