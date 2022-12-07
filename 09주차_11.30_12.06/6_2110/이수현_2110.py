# 2110 : 공유기 설치
# sys.readline 안쓰면 시간초과 발생

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input().rstrip()) for _ in range(n)]

house.sort()

# 끝점은 집들 사이 거리의 최댓값
start, end = 1, (house[-1] - house[0])

result = 0
while start <= end:
    mid = (start + end) // 2
    current = house[0]
    # 시작점은 공유기 설치하므로 1로 초기화
    count = 1

    for i in range(1, len(house)):
        # 현재 위치와 다음 집 사이의 거리가 mid 이상인 위치에만 공유기 설치
        if house[i] - current >= mid:
            # 현재 위치 바꾸기
            current = house[i]
            count += 1
    
    # 공유기가 부족하면 mid 거리 크게
    if count >= c:
        result = mid
        start = mid + 1
    # 공유기가 남으면 mid 거리 작게
    else:
        end = mid - 1

print(result)