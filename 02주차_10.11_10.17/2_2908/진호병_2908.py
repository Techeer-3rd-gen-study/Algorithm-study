n1, n2 = input().split()

m1 = list(reversed(n1))
m2 = list(reversed(n2))

result1 = ""
result2 = ""

for i in m1:
    result1 += i
for i in m2:
    result2 += i

if result1 > result2 : 
    print(result1)
else : 
    print(result2)

