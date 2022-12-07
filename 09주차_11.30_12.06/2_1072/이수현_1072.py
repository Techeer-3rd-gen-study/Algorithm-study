# 1072 : 게임

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x

# 승률이 절대 오르지 않을 경우
if z >= 99:
    print(-1)
else:
    answer = 0
    start, end = 1, sys.maxsize

    while start <= end:
        mid = (start + end) // 2
        new_z = (y + mid) * 100 // (x + mid)

        # 원래 승률보다 작거나 같을 경우
        if new_z <= z:
            start = mid + 1
        # 승률이 변한 경우(원래 승률보다 큰 경우)
        else:
            answer = mid
            end = mid - 1
            
    print(answer)

    
