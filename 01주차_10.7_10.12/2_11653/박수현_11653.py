num = int(input())

list = []

for i in range(2, num+1):
  if num == 0:
    break
  for j in range(2, num+1):
    if num%j == 0:
      list.append(j)
      num = int(num/j)
      break

for i in range(0, len(list)):
  print(list[i])
