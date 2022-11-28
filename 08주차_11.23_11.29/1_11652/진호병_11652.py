n = int(input())

card = {}

for i in range(n):
    node = int(input())
    if node in card : 
        card[node] += 1
    else :
        card[node] = 1

result = sorted(card.items(), key=lambda x:(-x[1], x[0]))
# items를 입력값으로 받고, 정렬 기준 key를 lamda를 이용하여-x[1], x[0]순으로 한다.
# 즉, x[1] (카드의 개수)의 -(내림차순)으로 정렬하고
# x[0] (카드 숫자)의 오름차순으로 정렬한다.

print(result[0][0])