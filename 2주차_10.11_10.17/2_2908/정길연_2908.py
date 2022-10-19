# 두 수 input
# string으로 받은 다음에 뒤집어주기

a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else :
    print(b)