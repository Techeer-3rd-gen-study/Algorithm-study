# 개미전사 p.220 

# 정수 N 입력받기
n = int(input())

# 리스트 입력 받기 
ary = list(map(int,input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = ary[0]
d[1] = max(ary[0], ary[1])
for i in range(2,n):
    d[i] = max(d[i - 1], d[i - 2] + ary[i])

# 계산된 결과 출력
print(d[n - 1])

