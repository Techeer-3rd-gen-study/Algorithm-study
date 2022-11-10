# 4-1. 상하좌우

import sys
input = sys.stdin.readline

n = int(input().rstrip())
x, y = 1, 1
plans = input().rstrip().split()

# LRUD에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

# 이동 계획 확인
for plan in plans:
    # 이동 후 좌표
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue

    # 이동 
    x, y = nx, ny

print(x, y)
