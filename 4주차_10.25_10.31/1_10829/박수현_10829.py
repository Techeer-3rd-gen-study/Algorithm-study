n = int(input())

s = ""

while n!=1 and n!=0:
    s = s+str(n%2)
    n = n//2

if n==1:
    s = s + "1"
elif n==0:
    s = s + "0"

print(int(s[::-1]))
