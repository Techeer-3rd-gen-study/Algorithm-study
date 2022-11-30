# 수 고르기

N, M = map(int, input().split()) # 정수 개수, 차이
lst = [int(input()) for _ in range(N)]

lst.sort() # 정렬 
start, end = 0, 0
result = int(2e9) # 큰 수

while start < N and end < N: # 인덱스가 N보다 작다.
    if lst[end] - lst[start] < M: # M보다 작을 때
        end += 1 # 끝점 인덱스 +1
    else: # M보다 클 때
        result = min(result, lst[end] - lst[start]) # result에 더 작은 값 저장
        start += 1 # 시작점 인덱스 +1

print(result)