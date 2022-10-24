n, k = map(int, input().split()) # n > coin_types // k = price

data = [] # 정렬 안된 coin_types 리스트 

for i in range(n): # coin_types 리스트로 만들기 
    data.append(int(input()))

coin_types = list(reversed(data)) # 인덱스 큰 수 부터 나오도록 정렬

count = 0 

for i in coin_types :
    count += k // i # k // i 는 changes 나누기 i 했을 때 몫을 나타냄 즉, 동전 갯수를 더해감
    k %= i # 나머지돈을 i로 줄수 있는 만큼 주고난 후의 남은 돈

print(count)
