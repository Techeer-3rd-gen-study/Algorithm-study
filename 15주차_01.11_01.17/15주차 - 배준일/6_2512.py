# 예산

N = int(input()) # 지방의 수

budget = list(map(int, input().split())) # 각 지방의 예산요청

M = int(input()) # 총 예산

start, end = 1, max(budget)

def is_successed(budget, mid):
    sum_money = 0

    for money in budget: # 예산과 mid 값 비교 후 작은 값 더하기
        sum_money += min(mid, money)

    return sum_money <= M # sum이 총 예산보다 작으면 True, 크면 False

while start <= end:
    mid = (start + end) // 2

    if is_successed(budget, mid):
        start = mid + 1
        
    else:
        end = mid - 1


print(end)