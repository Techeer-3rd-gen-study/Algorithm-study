# 효율적인 화폐 구성 p.226

# 정수 n, m 을 입력받기 
n, m  = map(int, input().split())

# n개의 화폐 단위 정보를 입력받기
ary = []
for i in range(n):
    ary.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = 0
for i in range(n):
    for j in range(ary[i], m + 1):
        if d[j - ary[i]] != 10001:
            d[j] = min(d[j], d[j - ary[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001 :
    print(-1)
else :
    print(d[m])
