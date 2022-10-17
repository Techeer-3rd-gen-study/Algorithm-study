num = input().split(" ")

num1 = list(num[0])
num2 = list(num[1])

sangsooNum1 = ""
sangsooNum2 = ""

for i in range(2, -1, -1) :
  sangsooNum1 = sangsooNum1 + num1[i]
  sangsooNum2 = sangsooNum2 + num2[i]

sangsooNum1 = int(sangsooNum1)
sangsooNum2 = int(sangsooNum2)

if sangsooNum1 > sangsooNum2:
  print(sangsooNum1)
else:
  print(sangsooNum2)
