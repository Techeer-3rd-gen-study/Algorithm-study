import sys
input = sys.stdin.readline

input_limit, money = map(int, input().split(" "))
list_money = [int(input()) for _ in range(0,input_limit)]
num = 0

for i in range(input_limit-1, -1, -1):
  if money//list_money[i] >= 1:
    r = money // list_money[i]
    money = money - list_money[i]*r
    num += r

print(num)
