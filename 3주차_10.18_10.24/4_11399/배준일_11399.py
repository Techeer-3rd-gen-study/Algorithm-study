# ATM

N = int(input())
P = list(map(int, input().split()))
result = 0
time = 0

P.sort() # P를 정렬

for i in P:
    time += i # Pn이 걸리는 시간
    result += time # Pn을 모두 더한 결과값

print(result)