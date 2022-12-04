import sys

input = sys.stdin.readline

K, N = map(int, input().split()) # 4개 존재 11개 만들기

lineArr = []

for _ in range(K):
    lineArr.append(int(input()))

start = 1
end = max(lineArr) # endpoint 가장 많이 짜를 수 있는 max 설정


answer = 0 

while start <= end:
    mid = (start + end) // 2
    lineCount = 0

    for i in lineArr :  # 선을 현재 mid로 나눠서 몇개 생성 가능한지 계산 
        lineCount += i // mid 

    if lineCount >= N : # 갯수가 맞거나 크면 더 많이 짤라볼 수 있음 == start 증가
        answer = mid
        start = mid+1
    else:
        end = mid - 1

print(answer)