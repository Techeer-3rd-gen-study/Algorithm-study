price = int(input())

coin_types= [500, 100, 50, 10, 5, 1]

changes  = 1000 - price # 1000 - 380 = 620 
count = 0 

for i in coin_types :
    count += changes // i # changes // i 는 changes 나누기 i 했을 때 몫을 나타냄 즉, 동전 갯수를 더해감
    changes %= i # 나머지돈을 i로 줄수 있는 만큼 주고난 후의 남은 돈

print(count)