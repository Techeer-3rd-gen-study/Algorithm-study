# 백준 5585 : 거스름돈 

changes = 1000 - int(input())  # 거스름돈
count = 0  # 거스름돈 개수 

money = [500,100,50,10,5,1]  # 엔화 리스트 
i = 0

while changes > 0 : 
    count += changes // money[i]  # 나누기 몫의 개수로 거스름돈 개수 추가 
    changes %= money[i]           # 나머지값 이용해서 거스름돈 변경 
    i += 1

print(count)

