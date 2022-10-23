# 큰 수의 법칙
import sys

n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

# 입력받은 배열 내림차순 정렬
data.sort(reverse=True)

result = 0

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count = count + m % (k + 1)

# 가장 큰 수 더하기
result = result + count * data[0]
# 두번째로 큰 수 더하기
result = result + (m - count) * data[1]

print(count)

# 단순한 방법
# while True:
#     # 가장 큰 수 k번(최대) 더하기
#     for _ in range(k):
#         if m == 0:
#             break
#         result = result + data[0]
#         # 더할 때 마다 m에서 1씩 빼기
#         m = m - 1
#     if m == 0:
#         break
#     # 2번째로 큰 수 1번 더하기
#     result = result + data[1]
#     m = m - 1
# print(result)
