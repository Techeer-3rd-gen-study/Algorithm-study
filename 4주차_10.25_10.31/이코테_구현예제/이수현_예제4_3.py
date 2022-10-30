# 왕실의 나이트

import sys

input = sys.stdin.readline

location = input()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한 지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)
