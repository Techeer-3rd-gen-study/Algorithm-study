# 피로도

import sys

a, b, c, m = map(int, sys.stdin.readline().split())
day = 0
fatigue = 0
result = 0

# 24 시간동안 실행
while day != 24:
    # 1시간 일함
    day = day + 1

    # 1시간당 쌓이는 피로도와 이전의 피로도가 m보다 작다면(아직 일할수있음)
    if a + fatigue <= m:
        # 1시간당 일한 양 추가
        result = result + b
        # 1시간당 쌓이는 피로도 추가
        fatigue = fatigue + a

    # 번아웃
    else:
        # 피로도 해소
        if fatigue >= c :
            fatigue = fatigue - c

        # 피로도는 0보다 작아질 수 없으므로 0으로 초기화
        else:
            fatigue = 0

print(result)