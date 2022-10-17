# 화성 수학

import sys
input = sys.stdin.readline

T = int(input().rstrip())
result = 0

for _ in range(T):
    op = input().rstrip().split() # 한 줄을 리스트로 받아옴
    for i in op:
        if i == '@':
            result *= 3
        elif i == '%':
            result += 5
        elif i == '#':
            result -= 7
        else: # 숫자일 때 
            result = float(i)
    print("{:.2f}".format(result))
    # print(round(result, 3))
    result = 0 # 출력이 끝난 결과 초기화
