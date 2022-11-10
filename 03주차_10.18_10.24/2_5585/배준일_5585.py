# 거스름돈

money_list = [500, 100, 50, 10, 5, 1] # 잔돈 리스트
changes = 1000 - int(input()) # 타로가 지불하고 남은 거스름돈
changes_num = 0 # 거스름돈 개수

while changes > 0: 
    for i in range(len(money_list)):
        money = money_list[i] # 잔돈

        if changes - money >= 0:
            changes -= money # 거스름돈에서 잔돈 빼기
            changes_num += 1 # 거스름돈 개수++
            break # for문 빠져나가기
        else:
            continue # for문 진행

print(changes_num)