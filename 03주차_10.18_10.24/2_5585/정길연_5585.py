# 거스름돈 개수 가장 작게, 몇 갠지 출력
# 500 100 50 10 5 1

change = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
ans = 0

for i in money:
    ans += change // i
    change %= i

print(ans)