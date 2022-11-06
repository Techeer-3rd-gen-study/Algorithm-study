import math

a = input().split(" ")

max = math.gcd(int(a[0]), int(a[1]))
min = math.lcm(int(a[0]), int(a[1]))

print(max)
print(min)
