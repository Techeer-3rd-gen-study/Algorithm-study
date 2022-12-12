import sys

input = sys.stdin.readline

N, C = map(int, input().split())

house = []

for _ in range(N):
  house.append(int(input()))

house.sort()

start = 1
end = house[-1] - house[0] # 최대값

result = 0

while (start <= end) : 
  
  mid = (start + end) // 2 # 공유기 간의 거리
  old = house[0]
  count = 1

  for i in range(1, len(house)):
    if house[i] >= old + mid:
      count += 1
      old = house[i]
    
    if count >= C :  # 그것보다 많이 설치할수 있으면
      start = mid + 1
      result = mid
    else : 
      end = mid - 1

print(result, "result")



