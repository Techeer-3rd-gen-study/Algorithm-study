# 2512번 : 예산 


import sys
input = sys.stdin.readline

n = int(input())  # 지방 수
request = list(map(int, input().split())) # 예산 요청
m = int(input()) # 총 예산 

start = 0
end = max(request)
answer = 0  

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in request:
        if i >= mid:
            total += mid
        else:
            total += i
    if total <= m:
            answer = mid
            start = mid + 1
    else:
        end = mid - 1

print(answer)