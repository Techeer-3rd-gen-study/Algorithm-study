str = list(input())
b = 0

for i in range(0, len(str)):
  if str[i] != str[len(str)-i-1]:
    b = 0
    break
  else:
    b = 1

print(b)
