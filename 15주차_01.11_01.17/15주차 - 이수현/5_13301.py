# 13301 : 타일 장식물

n = int(input())

# dp 테이블 초기화
d = [0] * 81

d[1] = 1
d[2] = 1

for i in range(3, n + 1):
    # 피보나치 수열 점화식
    d[i] = d[i - 1] + d[i - 2]

# 직사각형 넓이 출력
print((d[n] + d[n] + d[n - 1]) * 2)