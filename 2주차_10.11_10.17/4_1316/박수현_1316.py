n = int(input())
num = 0
b = True

for i in range(0, n):
  str = input()
  for j in range(0, len(str)):
    s = str.rfind(str[j])
    if s == j:
      b = True
    else:
      for k in range(j, s):
        if str[k]!=str[s]:
          b = False
          break
        else:
          b = True
    if b == False:
      break
  if b:      
    num = num+1

print(num)
