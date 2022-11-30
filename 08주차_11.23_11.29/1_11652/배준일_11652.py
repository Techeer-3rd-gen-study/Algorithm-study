# 카드

N = int(input()) # 카드의 개수

card = {}

for _ in range(N):
    card_num = int(input())

    if card_num in card: # 카드 번호가 있는 경우
        card[card_num] += 1
    else: # 카드 번호가 없는 경우
        card[card_num] = 1

card = sorted(card.items(), key = lambda x : (x[0], -x[1])) # x[0] = 카드 번호 -> 오름차순, x[1] = 빈도 수 -> 내림차순

print(card[0][0])
