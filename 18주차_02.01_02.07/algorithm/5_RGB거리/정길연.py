n = int(input())

house = []
for i in range(n):
    house.append(list(map(int, input().split())))

# 이 전 값중 min값과 자기자신 더해서 초기화
for i in range(1, len(house)):
    house[i][0] = house[i][0] + min(house[i-1][2], house[i-1][1])
    house[i][1] = house[i][1] + min(house[i-1][2], house[i-1][0])
    house[i][2] = house[i][2] + min(house[i-1][0], house[i-1][1])

answer = min(house[n-1][0], house[n-1][1], house[n-1][2])

print(answer)