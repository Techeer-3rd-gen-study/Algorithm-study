#  카드2

from collections import deque

card = deque([i for i in range(1, int(input())+1)])

while len(card) != 1:
    card.popleft() # 제일 위에 있는 카드 버리기
    up_second = card.popleft() # 두번째 제일 위에 있는 카드 
    card.append(up_second) # 두번째 제일 위에 있는 카드 제일 아래로 옮기기

print(*card) # 리스트 안 요소 출력
