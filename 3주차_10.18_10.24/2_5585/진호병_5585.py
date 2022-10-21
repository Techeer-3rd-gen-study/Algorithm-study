price = int(input())

coin_types= [500, 100, 50, 10, 5, 1]

changes  = 1000 - price # 1000 - 380 = 620 
count = 0 

for i in coin_types :
    count += changes // i
    changes %= i

print(count)