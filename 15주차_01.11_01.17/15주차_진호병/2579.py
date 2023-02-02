n = int(input())

d = [0] * 301

stair = [0] * 301

for i in range(n):
  stair[i] = (int(input()))


d[0] = stair[0]

d[1] = stair[0] + stair[1]

d[2] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range(3,n):
  d[i] = max(d[i-3] + stair[i-1]+ stair[i], d[i-2] + stair[i])
  # 경우의 수가 2가지다. 
  # 1. 시작점(세칸 전)에서 두칸 뛰고 한칸 뛰어서 오는 경우 
  # 2. 시작점(두칸 전)에서 연속으로 두번 한칸 뛰어서 오는 경우
print(d[n-1])
