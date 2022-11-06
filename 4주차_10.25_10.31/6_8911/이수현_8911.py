# 거북이

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dir = deque([[-1,0],[0,1],[1,0],[0,-1]])

for _ in range(n):
    control = input().strip()
    max_x, max_y, min_x, min_y = 0,0,0,0
    x, y = 0,0
    
    for c in control:
        # 왼쪽 회전
        if c == 'L':
            dir.rotate(1)
        # 오른쪽 회전
        elif c == 'R':
            dir.rotate(-1)
        # 한 눈금 앞으로
        elif c == 'F':
            x = x + dir[0][0]
            y = y + dir[0][1]
        # 한 눈금 뒤로
        elif c == 'B':
            x = x - dir[0][0]
            y = y - dir[0][1]

        # x, y 최댓값/최솟값 구하기    
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)

    print(abs(max_x - min_x) * abs(max_y - min_y))