import sys

n,m =map(int, input().split())

start = 0
end = 0
result = sys.maxsize

array = []

for _ in range(n):
    array.append(int(input()))


array.sort()

while start < n and end<n: 
    # 투 포인터 (여기서 사용된건 배열이 정렬이 되어있어서 가능한 알고리즘임)
    # 시작점과 끝점을 정하고 interval이 조건보다 작으면 End를 크면 start를 +1 씩 해가며 탐색하는 것
    interval = abs(array[start]-array[end]) 
    if interval == m : 
        result = interval # 조건과 같으면 가장 최소값으로 break
        break
    elif interval > m : # 크면 큰 값 중에 최소값을 저장
        result = min(interval, result)
        start += 1
    else:
        end += 1

print(result)