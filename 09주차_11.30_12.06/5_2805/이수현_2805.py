# 2805 : 나무 자르기

n, m = map(int, input().split())
height = list(map(int, input().split()))

start, end = 0, max(height)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in height:
        # 잘린 나무 계산
        if x > mid:
            total += x - mid
            
    # 나무가 충분한 경우
    if total < m:
        end = mid - 1
    # 나무가 부족한 경우
    else:
        result = mid
        start = mid + 1

print(result)