# 백준 11047 : 동전 0
# 5585:거스름돈 문제의 변형, 동전 종류를 input값으로 추가함 

n, price = map(int,input().split())  # 동전개수, 금액 

coin = []   
for _ in range(n):                  # 동전 종류 입력 
    coin.append(int(input()))  

coin.sort(reverse=True)              # 역순으로 바꿔주어 큰 순서대로 정렬 

count = 0  
i = 0

while price != 0 : 
    count += price // coin[i]  # 나누기 몫의 개수로 거스름돈 개수 추가 
    price %= coin[i]           # 나머지값 이용해서 거스름돈 변경 
    i += 1

print(count)

