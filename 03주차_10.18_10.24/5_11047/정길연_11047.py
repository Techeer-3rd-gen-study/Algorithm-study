# 틀렸다 하네요.. 왜일까요..? 

N, money = map(int, input().split())

units = list()

for _ in range(N) : 
    units.append(int(input(_)))

# unit는 오름차순으로 주어지므로, 역방향으로 정렬
units = sorted(units, reverse=True)

ans = 0

for unit in units:
    # 클 때 고려 X
    if money >= unit:
        ans += money 
        money %= unit 
        if money <= 0: 
       		break

# for i in range(N):
#     ans += money // units[i]
#     money %= units[i]

print(ans) 