# 13301번 : 타일 장식물 
# 작은 직사각형 한변의 길이 -> 피보나치
# 둘레 길이 : 4, 6, 10, 16, 26 -> 피보나치와 비슷한 원리 점화식 

# 방법1) 보텀업 프로그래밍
n = int(input())

d = [0] * 81

d[1] = 4
d[2] = 6

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])



'''
# 방법2) 탑다운 다이나믹 프로그래밍
n = int(input())

d = [0] * 81

def fibo(x):
    # 종료 조건
    if x == 1 :
        return 4
    if x == 2 :
        return 6

    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산한 적 없는 문제 일 경우 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(n))
'''
