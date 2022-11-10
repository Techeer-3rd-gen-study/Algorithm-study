# 트럭주차

import sys
input = sys.stdin.readline
a, b, c = map(int, input().rstrip().split())
# 주차 시간 체크할 변수
time_table = [0] * 100

for _ in range(3):
    time_in, time_out = map(int, input().rstrip().split())
    # 시간과 다르게 인덱스는 0부터 시작하므로 -1
    for i in range(time_in - 1, time_out - 1):
        # 주차 시간 체크
        time_table[i] += 1
money = 0

for i in time_table:
    if i == 1:
        money += a * i
    elif i == 2:
        money += b * i
    elif i == 3:
        money += c * i
print(money)

