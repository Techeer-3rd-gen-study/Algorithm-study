# 숫자 카드 게임
import sys

a, b = map(int, sys.stdin.readline().split())
result = 0

for i in range(a):
    data = list(map(int, sys.stdin.readline().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 중 가장 큰 수 찾기
    result = max(result, min_value)

print(result)