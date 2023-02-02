# 1072번 : 게임

import sys
input = sys.stdin.readline

x, y = map(int,input().split())
win = (y * 100) // x  # 승률 
count = 0

if win >= 99:
    print(-1)

else:
    count = 0
    start =1
    end = 1000000000

    # 승률 계산
    while start <= end:
        mid = (start + end) // 2

        if (y + mid)*100 // (x + mid) > win:
            count = mid
            end = mid - 1
        else:
            start = mid + 1

    print(count)