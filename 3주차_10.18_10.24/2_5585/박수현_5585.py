money = 1000 - int(input())

num = 0

while money > 0:
  num += 1
  if money >= 500:
    money -= 500
    continue
  elif money >= 100:
    money -= 100
    continue
  elif money >= 50:
    money -= 50
    continue
  elif money >= 10:
    money -= 10
    continue
  elif money >= 5:
    money -= 5
    continue
  elif money >= 1:
    money = money - 1
    continue

print(num)
