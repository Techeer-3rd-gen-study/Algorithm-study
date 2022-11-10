num = int(input())
str = []

for i in range(0, num):
  str.append(input())

for i in range(0, num):
  ss = str[i].split(" ")
  r = int(ss[0])
  s = list(ss[1])
  for i in range(0, len(s)):
    print(s[i]*r, end="")
  print()


