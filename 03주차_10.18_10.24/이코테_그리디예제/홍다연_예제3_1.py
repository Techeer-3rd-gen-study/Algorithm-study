# 홍다연_예제_3_1 : 거스름돈

changes = int(input())  # 거스름돈
count = 0  # 동전 개수

money = [500,100,50,10]
i = 0

while changes > 0 : 
    count += changes // money[i]  # 동전 개수 추가 
    changes %= money[i]           # 나머지값 이용해서 거스름돈 변경 
    i += 1

print(count)
