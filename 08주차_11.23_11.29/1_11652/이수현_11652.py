# 11762 : 카드

import sys
input = sys.stdin.readline

n = int(input())
card_dic = {}

for _ in range(n):
    card = int(input())
    # { 카드값 : 카드 개수 }
    # card(키)가 카드 딕셔너리에 존재하면 
    if card in card_dic:
        card_dic[card] += 1
    # 존재하지 않으면 딕셔너리에 추가해주기
    else:
        card_dic[card] = 1
    
# 카드 개수는 내림차순, 카드 숫자는 오름차순 정렬
# (첫 번째 요소, 두 번째 요소), 첫 번째 요소가 우선순위
result = sorted(card_dic.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])