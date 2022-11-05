A,B,C = map(int, input().split())

price = [0 for _ in range(100)] # 최대 100까지 있어서 미리 만들어둠
 
sum = 0

for i in range(3): # 총 3대 반복
    hi, bye = map(int, input().split())
    for j in range(hi,bye): # ex. 1~6이면 그 인덱스에 해당하는 곳에 +1 해서 차량 한대를 의미함
        price[j] += 1

for i in range(100): # 위에서 저장한 배열을 차량 수에 따라 총 비용 계산
    if price[i] == 1 :
        sum += A
    if price[i] == 2 :
        sum += B*2
    if price[i] == 3 :
        sum += C*3

print(sum)