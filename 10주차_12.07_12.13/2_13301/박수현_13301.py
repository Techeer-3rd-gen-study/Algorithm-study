# f(n) = f(n-1) + f(n-2)
a1 = 4
a2 = 6
dp = 0
n = int(input())
if n==1: 
    dp = a1
elif n==2:
    dp = a2
else:
    for i in range(2,n):
        dp = a1+a2
        a1 = a2
        a2 = dp
print(dp)